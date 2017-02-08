#! python

from functools import wraps


def decorated_novar(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print 'decorated_novar.wrapper.begin'
        obj = f(*args, **kwargs)
        print 'decorated_novar.wrapper.end'
        return obj
    return wrapper


def decorated_var(key):
    if isinstance(key, int):
        def _wrapper(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                print 'decorated_var.wrapper.begin, int'
                obj = f(*args, **kwargs)
                print 'decorated_var.wrapper.end, int'
                return obj
            return wrapper

    else:
        def _wrapper(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                print 'decorated_var.wrapper.begin, other'
                obj = f(*args, **kwargs)
                print 'decorated_var.wrapper.end, other'
                return obj
            return wrapper
    return _wrapper


@decorated_var("")
@decorated_var(1)
@decorated_novar
def foo(a, b):
    print a, b


@decorated_novar
class bar(object):
    pass

if __name__ == '__main__':
    foo("Hello", "World")
    print foo.__name__
    print type(bar)
    print type(bar())
