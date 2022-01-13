def rot13(s: str) -> str:
    new_cs = []

    for c in s:
        if 'a' <= c <= 'z':
            new_c = chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            new_c = chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            new_c = c
        new_cs.append(new_c)

    return ''.join(new_cs)
