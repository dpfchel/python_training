
import pytest
from pony.orm import *
import re
import string


class Complex_data():
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex_data):
            new_real = self.real + other.real
            new_imag = self.imag + other.imag
        elif isinstance(other, int) or isinstance(other, float):
            new_real = self.real + other
            new_imag = self.imag
        else:
            raise TypeError("unreal add")
        return Complex_data(new_real, new_imag)

    def __eq__(self, other):
        if isinstance(other, Complex_data) and self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False

    def __str__(self):
       return "Complex data real = " + str(self.real) + " imag = " + str(self.imag)


def test_1():
    a = Complex_data(2,3)
    b = Complex_data(4,4)
    null_my = Complex_data()
    int_n = 5
    float_m = 4.03
    assert a + b == Complex_data(6,7)

if __name__ == '__main__':
    test_1()




