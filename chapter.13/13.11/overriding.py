#!python


class P(object):
    def __init__(self):
        print "Calling P's constructor"

    def foo(self):
        print 'Hi, I am P-foo()'

p = P()
p.foo()


class C(P):
    def __init__(self):
        print "Calling C's constructor"
        # P.__init__()
        super(C, self).__init__()

    def foo(self):
        # P.foo(self)
        super(C, self).foo()
        print 'Hi, I am C-foo()'

c = C()
c.foo()

P.foo(c)
