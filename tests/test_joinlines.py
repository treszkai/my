from my import joinlines

words = {'foo', 'fuzzy-guzzy', 'goodbye'}


def test_process():
    result = joinlines.process_lines(
        ['bar foo', 'fuzzy fuzzy', 'guzzy'], words
    )
    assert 'bar foo fuzzy fuzzy guzzy' == result

def test_process_hyphenation():
    result = joinlines.process_lines(
        ['bar foo', 'fuzzy fuzzy-', 'guzzy good-', 'bye pal.'], words
    )
    #                      hyphened  / joined
    assert 'bar foo fuzzy fuzzy-guzzy goodbye pal.' == result


def test_process_empty_line():
    result = joinlines.process_lines(
        ['bar foo', ' ', 'whatevs'], words
    )
    assert 'bar foo whatevs' == result

def test_process_single_line():
    result = joinlines.process_lines(
        ['bar foo'], words
    )
    assert 'bar foo' == result
