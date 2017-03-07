import dis


def foo():
    j = 2
    try:
        i = 1
        1/0
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        print i, j
        return 4

dis.dis(foo)
print "===================="
foo()
