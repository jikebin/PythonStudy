'''
生成器：
大纲：列表生成式 生成器的两种创建方式 可迭代对象(for循环) yield关键字的三个相关方法(__iter__() __next__() send())
列表生成式：[]
    1.简单：[x for x in range(10)]
    2.一般：[x*2 for x in range(10)]
    3.复杂：
        foo = lambda a : a**2
        [foo(x) for x in range(10)]
生成器(generator):
    创建生成器(generator)：
        1.(x for x in range(10))
        2.使用 yield关键字
    生成器特点：
        1.生成器内部方法：__next__ 和 __iter__
        2.生成器的底层的单项链表
        3.生成器只是数据指针，而不存储数据,所以节省内存空间（随时调用，随时开辟空间）
    生成器调用：
        1.调用一次：next()
        2.调用多次：for
可迭代对象：
    可迭代对象特点：
        内部带有：__iter__方法的，都是可迭代对象
    for循环特点：
        1.for循环后面跟的都是可迭代对象
    for循环做的三件事
        1.调用iter()创建迭代器
        2.循环调用next()获取数据
        3.捕获异常，并结束循环
    可迭代对象有：
        列表、元组、字典、字符串、文件、集合、生成器(generator)、迭代器(iterable)
yield关键字的三个关联方法：
    说明：函数内部含有yield关键字，就会有：__iter__ __next__ 和 send() 三个方法
    __iter__ ：代表可迭代对象
    __next__：代表生成器
    send() : 功能与 next()类似，但是可以给yield传递参数
-------------------------------------------------------------------------------------------
'''
#列表生成式
# li = [x**2 for x in range(5)]
# print(li)
# def foo(n):
#     return n+2
# li2 = [foo(x) for x in range(4)]
# print(li2)
#-------------------------------------------------------------------------------------
#生成器两种方式
# li = (x**3 for x in range(4))
# print(li)  #<generator object <genexpr> at 0x0000000000D6A150>
# print(next(li))  # 0
#---------------
def foo():
    print("ok1")
    value = yield 1
    print(value)
    print("ok2")
    yield 2
f = foo()
print(f) #<generator object foo at 0x0000000000D4A150>
#三种调用方式
#print(next(f))  #方式1
# for i in f:  #方式2
#     print(i)
#-------------
# value1 = f.send(None) #方式三
# value2 = f.send("测试")
# print(value1,"---",value2)
#----------------------------
iter1 = iter(f)
print(next(iter1)) #生成器，在调用__iter__方法后，返回值对象仍然可以调用next()方法，正常输出
