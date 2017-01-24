#!python


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "val must be a float"
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


# rfm = RoundFloatManual(42)

rfm = RoundFloatManual(4.2)
print rfm
print repr(rfm)
