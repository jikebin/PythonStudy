'''
装饰器前的三个准备：作用域、高阶函数、闭包
    1.作用域：LEGB(主要是 内嵌作用域L 和 局部作用域E)
    2.高阶函数：函数名可以作为参数和返回值
    3.闭包：公式：闭包 = 内部函数 + 外部变量(局部作用域变量)
          定义：如果在一个内部函数里，对外部作用域(不是全局作用域)的变量进行引用，那么内部函数就算是——闭包。
-----------------------------------------------------------------------
装饰器：
    特点：遵守开闭原则，扩展某个函数功能的同时，不改变函数源码 和 调用方式。
    实现思想：
        1.入口和出口都是：函数(高阶函数)
        2.通过内部函数实现功能扩展(闭包)
        3.将扩展后的函数重新赋值给原函数
装饰器的三种实例：
    1.函数无参数，装饰器无参数 (简单)嵌套一层
    2.函数带参数，装饰器无参数 (一般)嵌套一层加参数
    3.函数带参数，装饰器带参数 (困难)嵌套两层
'''
#---------------------------------------------------------------------------
#简单装饰
import time
def foo():
    print("请稍等...")
    time.sleep(2)
#定义装饰器，实现计算函数运行时间的功能扩展
def show_time(fun):
    def inner():
        star = time.time()
        fun()
        end = time.time()
        print("运行时间为：",(end - star))
    return inner
foo = show_time(foo)
#测试
foo()
# #----------------------------------------------------------------------------
#python优化后的装饰器
@show_time
def foo2():
    print("优化方法...")
    time.sleep(1)
#测试
foo2()
#---------------------------------------------------------------
#一般装饰器：函数带参数，装饰器不带参数
#定义装饰器：
def show_time(func):
    def inner(*args): #定义函数参数
        star = time.time()
        ret = func(*args)
        end = time.time()
        print("运行时间为：",(end - star))
        return ret
    return inner
#定义函数
@show_time
def add(*args):
    sum1 = 0
    for i in args:
        sum1 +=i
    time.sleep(1)
    return sum1

#测试
value =add(*range(1,10))
print(value)
#---------------------------------------------------------------------------------
#困难：给装饰器加参数：
def flag(fl): #装饰器的参数
    def show_time(func):
        def inner():
            start = time.time()
            func()
            end = time.time()
            print("运行时间：",(end - start))
            #注意，这里面可以使用fl参数，这是闭包现象
        return inner
    return show_time

@flag("ture") #该方法等价于 @show_time
def foo():
    print("测试")
#说明：当定义flag("ture")时，会首先运行该方法，而返回的参数则是 show_time函数名(高阶函数)
#运行
foo()
