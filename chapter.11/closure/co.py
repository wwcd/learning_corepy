#!/usr/bin/env python

from random import randint


def simpleGen():
    yield 1
    yield '2 -- > punch'

myG = simpleGen()
print myG.next()
print myG.next()
# myG.next()


def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList)-1))

for i in randGen(['rock', 'paper', 'scissors']):
    print i
