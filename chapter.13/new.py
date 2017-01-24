#!/usr/bin/env python

import sys


class AddrBookEntry(object):
    'address book entry class'

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for:', self.name

    def updatePhone(self, newph):
        self.phone = newph
        print 'Updated phone # for:', self.name


class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'

    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name


john = AddrBookEntry('john', '12346')
john.updatePhone('789012')

print sys.path


class C(object):
    foo = 100


print C.foo
c = C()
C.foo = 200
print C.foo
print c.foo


class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'

    def showMyVersion(self):
        print MyClass.myVersion

print dir(MyClass)
print MyClass.__dict__
