from my import rot13


def test_rot13():
    assert rot13('') == ''
    assert rot13('abzABZ123 űÚ') == 'nomNOM123 űÚ'
