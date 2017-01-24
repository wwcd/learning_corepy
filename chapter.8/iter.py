#! /usr/bin/evn python


class C(object):
    def __getitem__(self, i):
        if i < 10:
            return i
        else:
            raise StopIteration


if __name__ == '__main__':
    c = C()
    a = iter(c)
    for i in a:
        print i
