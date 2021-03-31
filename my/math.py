from math import *


def d(rad: float) -> float:
    """Convert radians to degrees"""
    return rad / pi * 180

def r(deg: float) -> float:
    """Convert degrees to radians"""
    return deg / 180 * pi

def cotan(x):
    """Cotangent"""
    return 1 / tan(x)

def dsin(deg):
    """Sine with argument in degrees"""
    return sin(r(deg))

def dcos(deg):
    """Cosine with argument in degrees"""
    return cos(r(deg))

def dtan(deg):
    """Tangent with argument in degrees"""
    return tan(r(deg))

def dcotan(deg):
    """Cotangent with argument in degrees"""
    return cotan(r(deg))

