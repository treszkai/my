from my import math

from pytest import approx


def test_d():
    assert math.d(0) == 0
    assert math.d(math.pi/2) == approx(90)

def test_r():
    assert math.r(0) == 0
    assert math.r(90) == approx(math.pi/2)

