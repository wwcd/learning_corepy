#! python

import unittest
# import os
from functools import wraps
from copy import deepcopy

options = {"K": 100}


class override_settings(object):
    def __init__(self, **kwargs):
        self.options = kwargs
        self._options = {}
        pass

    def __call__(self, decorated):
        if isinstance(decorated, type):
            print 'cls override_settings: decorated class', decorated.__name__
            # inner = type(
            #     decorated.__name__,
            #     (decorated,),
            #     {})
            return decorated
        elif callable(decorated):
            print 'cls override_settings: decorated call', decorated.__name__

            @wraps(decorated)
            def inner(*args, **kwargs):
                with self:
                    return decorated(*args, **kwargs)
            return inner
        else:
            raise TypeError('Cannot decorated type %s' % type(decorated))

    def __enter__(self):
        global options
        print '__enter__ 1'
        print "SELF:", self.options
        print "GLOBAL:", options
        self._options = deepcopy(options)
        options.update(self.options)
        print '__enter__ 2'
        print "SELF:", self.options
        print "GLOBAL:", options
        print '__enter__ 3'
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        global options
        print '__exit__ 1'
        print "SELF:", self.options
        print "GLOBAL:", options
        options = deepcopy(self._options)
        print '__exit__ 2'
        print "SELF:", self.options
        print "GLOBAL:", options
        print '__exit__ 3'
        pass


@override_settings(K=0)
class AAA(object):
    def foo(self):
        print 'AAA.foo'
    pass


a = AAA()
a.foo()


@override_settings(K=1)
class TestStringMethods(unittest.TestCase):
    @override_settings(K=2)
    def test_upper(self):
        print 'called test_upper'
        self.assertEqual('foo'.upper(), 'FOO')

    @override_settings(K=3)
    def test_isupper(self):
        print 'called test_isupper'
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @override_settings(K=4)
    def test_split(self):
        print 'called test_split'
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
