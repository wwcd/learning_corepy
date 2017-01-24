def f(d=0):
    c = 1
    print "hello", c


a = "*12345*&^%"
b = "*12345*&^%"
f()

print a is b


# >>> a=open('src_file.py','r').read()    #命令行模式中打开源文件进行编译
# >>> co=compile(a,'src_file','exec')
# >>> type(co)
