from pytest import approx

from my.stats import compare_ratios


def test_compare_ratios_float_tuple():
    assert compare_ratios(0.5, (15, 30)) == approx(0.5)
    assert compare_ratios(0.1, (29, 30)) > 0.99
    assert compare_ratios(0.9, (1, 30)) < 0.01

    assert compare_ratios((15, 30), 0.5) == approx(0.5)
    assert compare_ratios((29, 30), 0.1) < 0.01
    assert compare_ratios((1, 30), 0.9) > 0.99
