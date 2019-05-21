'''
说明：内置函数是系统自带的函数，可以在所有文件中直接使用，最常用的有：
  len() list() dutp() dict() str() set() 

1、这些函数的特点是不需要进行 import 模块导入就可以使用
2、像 os 等模块内的函数，则需要进行 import 模块导入才可以使用

两个概念：匿名函数、回调函数
  匿名函数：也就是没有名称的函数，特点是什么时候使用，什么使用创建，一般只使用一次
  回调函数：将函数名作为参数传递给另一个参数（高阶函数特性），这种函数就叫做回调函数。

常用的几个回调函数(内置函数)：
  filter(function,str)    #过滤
  map(function,str)       #修改
  说明：参数 str 指的是可迭代对象，可迭代对象会在 迭代器和生成器中讲到
'''
# 匿名函数在python中的使用：lambda
s1 = lambda a,b : a+b   # a,b 为参数 ：后面为返回值内容
print(s1(1,2))  # 输出：3

# 过滤器 filter
def my_filter(value):   # 定义过滤规则，将 'a' 过滤掉
    if value != 'a':
        return value
ret1 = filter(my_filter,['a','b','c','a'])
print(ret1)       # 迭代器对象，输出：<filter object at 0x7f9a62fd4780>
print(list(ret1)) # 输出：['b', 'c']

# map 修改数据
ret2 = map(lambda a:a+"admin",['a','b','c','d'])
print(ret2)         # 可迭代对象，输出:<map object at 0x7f078f5c09e8>
print(list(ret2))   # 输出：['aadmin', 'badmin', 'cadmin', 'dadmin']