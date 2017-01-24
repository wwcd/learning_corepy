#!python

import __builtin__


class P1(object):
    def foo(self):
        print 'called P1-foo()'


class P2(object):
    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print 'called C2-bar()'


class GC(C1, C2):
    pass

print GC.__mro__
print issubclass(GC, C2)
print issubclass(GC, P1)
print issubclass(C1, P1)
print issubclass(C2, P1)
print issubclass(C2, C1)

print dir(__builtin__)


print hash('a')
