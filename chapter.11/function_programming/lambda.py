#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print (lambda: 1)()


# a = 1 and 3
# print a

# a = lambda: 1 and 3
# print type(a)
# print a()

# i = 200
# def foo():
#     j = 100
#     # return lambda: i + j
#     return (j for _ in xrange(10))

# a = foo()
# for i in a:
#     print i

y = 100

class A(object):
    x = 1
    gen = (lambda x=x: (x for _ in xrange(10)))()
    fun = lambda self: self.x + y

print A.gen
print A().fun()
