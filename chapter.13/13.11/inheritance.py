#! /usr/bin/env python


class P(object):
    'P class'
    def __init__(self):
        print 'created an instance of ', self.__class__.__name__

    def foo(self):
        return 'P.foo()'


class C(P):
    pass

    def foo(self, name):
        return 'C.foo()' + name

    def __hash__(self):
        return 100


p = P()
print p.__class__
print P.__bases__
print P.__doc__
print dir(P)
print dir(p)
print p.__doc__

c = C()
print c.__class__
print C.__bases__
print C.__doc__

# print os.__doc__

print c.foo("123")

a = {}
a[c] = 1

c1 = C()
print "keys", a.keys(), c.__hash__()
print "keys", a.keys(), c.__hash__()

a[c1] = 2
print "keys", a.keys(), c1.__hash__()
print "keys", a.keys(), c1.__hash__()

a1 = {}
# a1[a] = 3
print dir(a1)
print a1.__hash__
print object.__hash__
print object.__hash__
print dir(c)
