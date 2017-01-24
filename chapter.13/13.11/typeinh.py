#! /usr/bin/python


class RoundFloat(float):
    def __new__(cls, val):
        # return float.__new__(cls, round(val, 2))
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

a = RoundFloat(1.5955)
print a, type(a)
b = RoundFloat(1.5945)
print b
print type(a + b)
print RoundFloat(-1.9955)
