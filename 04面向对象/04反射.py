'''
反射：
大纲：定义、常用内置方法
定义：
    定义:通过字符串的方式，操作对象的成员(类对象，模块对象 ... ...)
    说明：python中一切皆对象
常用内置方法：
    getattr(对象名,"成员名")              #成员名为字符串形式
    hasattr(对象名,"成员名")              #用于判断该对象成员是否存在
    setattr(对象名,"成员名",成员值)      #用于添加对象成员(在内存中)
    delattr(对象名,"成员名")              #用于删除对象成员（在内存中）

'''
class Demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

student = Demo("大黄",24)
print(getattr(student,"name"))
print(hasattr(student,"name"))
setattr(student,"sex","公")
print(getattr(student,"sex"))
delattr(student,"name")
print(hasattr(student,"name"))
