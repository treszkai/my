from my import joinlines

words = {'foo', 'fuzzy-guzzy', 'goodbye'}


def test_process():
    result = joinlines.process_lines(
        ['bar foo', 'fuzzy fuzzy-', 'guzzy good-', 'bye pal.'], words
    )
    assert 'bar foo fuzzy fuzzy-guzzy goodbye pal.' == result


def test_process_single_line():
    result = joinlines.process_lines(
        ['bar foo'], words
    )
    assert 'bar foo' == result
