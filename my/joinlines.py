from itertools import chain, pairwise
from pathlib import Path
import subprocess
import select
import sys


class Clipboard:
    def read(self):
        ...

    def write(self, text: str) -> None:
        ...


class LinuxClipboard(Clipboard):
    def read(self) -> str:
        return subprocess.run(
            ['xclip', '-selection', 'clipboard', '-o'], text=True, capture_output=True
        ).stdout

    def write(self, text: str):
        subprocess.run(['xclip', '-selection', 'clipboard', '-i'], text=True, input=text)


class MacClipboard(Clipboard):
    def read(self) -> str:
        return subprocess.run(['pbpaste'], text=True, capture_output=True).stdout

    def write(self, text) -> str:
        subprocess.run(['pbcopy'], text=True, input=text)


def add_line(line: str, lines: list[str], use_space: bool):
    if use_space:
        lines.append(line)
    else:
        lines.append(lines.pop() + line)


def load_words() -> set[str]:
    with open(Path(__file__).parent / 'words.txt') as f:
        return {line.strip() for line in f}


def read_text() -> list[str]:
    """Read text either from stdin or from clipboard, whichever comes first"""
    initial_clipboard = clipboard.read()
    print('Enter text or copy to clipboard:')

    while True:
        i, o, e = select.select([sys.stdin], [], [], 1)

        if i:
            x = sys.stdin.read()
            break
        else:
            x = clipboard.read()
            if x != initial_clipboard:
                print("Copied from clipboard:")
                print(x)
                break

    raw_lines = [line.strip() for line in x.splitlines()]
    return raw_lines


def process_lines(raw_lines: list[str], words: set[str]) -> str:
    lines = []
    use_space = True

    for line1, line2 in pairwise(chain(raw_lines, [''])):
        if line1.endswith("-"):
            word1 = line1.split()[-1]
            word2 = line2.split()[0]
            if word1 + word2 in words:
                add_line(line1, lines, use_space)
            else:
                add_line(line1.rstrip('-'), lines, use_space)

            use_space = False

        else:
            add_line(line1, lines, use_space)
            use_space = True

    return ' '.join(lines)


def handle_text(text):
    clipboard.write(text)

    print('\nCopied to clipboard:\n>>>\n')
    print(text)
    print('\n<<<\n')


def run():
    words = load_words()

    while True:
        try:
            raw_lines = read_text()
        except KeyboardInterrupt:
            break
        text = process_lines(raw_lines, words)
        handle_text(text)


if sys.platform.startswith('linux'):
    clipboard = LinuxClipboard()
elif sys.platform.startswith('darwin'):
    clipboard = MacClipboard()
else:
    raise NotImplementedError('Clipboard functionality implemented only for Linux and MacOS')


if __name__ == '__main__':
    run()
else:
    print(
        f'Importing {__name__} does not do anything. '
        'Run it as `$ python -m my.joinlines` from the terminal instead.',
        file=sys.stderr
    )
