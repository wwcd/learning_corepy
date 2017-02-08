class decorated_var(object):

    def __init__(self, **kwargs):
        print "inside decorated_var.__init__()"
        # f()  # Prove that function definition has completed

    def __call__(self, f):
        print "inside decorated_var.__call__()"
        if isinstance(f, type):
            return f
        elif callable(f):
            return f
        else:
            raise TypeError("invalid type %s" % dir(f))


class decorated_novar(object):
    def __init__(self, f):
        print "inside decorated_novar.__init__()"
        self.f = f

    # def __new__(self, f):
    #     print "inside __new__", f.__name__
    #     return f

    def __call__(self):
        print "inside decorated_novar.__call__()"
        if isinstance(self.f, type):
            return self.f()  # 对类的话进行实例化
        elif callable(self.f):
            return self.f()

    def __get__(self, instance, owner):
            return lambda *args, **kwargs: self.f(instance, *args, **kwargs)


print "===foo_func==="


# @decorated_novar
@decorated_var(K=1)
def foo_func():
    print "inside foo_func()"


print "===foo_cls==="


# @decorated_novar
@decorated_var(K=2)
class foo_cls(object):
    @decorated_novar
    # @decorated_var(K=4)
    def foo(self):
        print "inside foo_cls.foo"

print "===call foo_func==="

foo_func()

print "===call foo_cls==="

a = foo_cls()
a.foo()
