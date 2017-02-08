from imptee import foo, show
from imptee import bar

show()
foo = 123  # 怎么理解? show里面使用的foo是模型的命名空间
print 'foo from imptee:', foo
show()

bar()


def bar():
    print 'bar inside impter'

bar()
