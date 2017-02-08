#! /usr/bin/evn python


class C(object):
    pass
    # def __getitem__(self, i):
    #     if i < 5:
    #         return i
    #     else:
    #         raise StopIteration

    def __iter__(self):
        # return iter([1, 2, 3])
        return self

    def next(self):
        raise StopIteration

if __name__ == '__main__':
    c = C()
    a = iter(c)
    for i in a:
        print i

    # j = 0;
    # try:
    #        i = __getitem__(j)
    #        j += 1
    #        print i
    # except StopIteration:
    #     pass

    # it = C.__iter__()
    # try:
    #     while True:
    #         i = it.next()
    #         print i
    # except StopIteration:
    #     pass
