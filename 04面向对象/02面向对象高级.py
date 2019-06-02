'''
面向对象高级：
大纲：成员修饰符、特殊成员(方法)、创建类的类：type()
成员修饰符：
    默认为共有
    私有标志为：__成员名
特殊成员(方法)：
    重要特殊成员：
        __init__()          调用：类名()
        __dict__()          调用：对象名.__dict__()   功能：以字段的形式封装字段名和字段值
        __str__()           调用：str(对象名)
        __getitem__()       调用：对象名[key] or 对象名[start:end:sept]  接受类型不同
        __setitem__()       调用：对象名[key] = value
        __delitem__()       调用：del 对象名[key]
        __iter__()          调用：iter(对象名)  or  for ...
    其他特殊成员：
        __call__            调用：对象名()
        __new__             功能：创建对象，一般在__init__()之前被自动调用
        __next__            调用：next(对象名)
        __add__             调用：对象名1 + 对象名2
        __int__             调用：int(对象名)
        __del__             调用：del 对象名
创建类的类：type()
    1.python中的一切都是对象，类也是对象，类默认是type()的对象
    2.所有类都默认继承object类
    3.可以通过使用：metaclass=类，来指定该类是谁的对象(非type) 注意：类的类要继承type
    4.初始化的完整顺序：__init__  __call__  __new__  __init__
'''
# class My_Type(type):
#     def __init__(self,*args,**kwargs):
#         print("这是创建类的类:__init__")
#     def __call__(self, *args, **kwargs):
#         print("初始化第一步：__call__")
#         obj = self.__new__(self, *args, **kwargs)
#         self.__init__(obj)


# class demo(object,metaclass=My_Type):
#     def __init__(self):
#         print("完成初始化")
#     def __new__(cls, *args, **kwargs):
#         print("初始化第二步：创建对象，__new__")
#         return object.__new__(cls, *args, **kwargs)
#     def __add__(self, other):
#         pass

# d = demo()
#------------------------------------------------------------------------------------
# __dict__()
# 调用：对象名.__dict__()
# 功能：以字段的形式封装字段名和字段值
# __str__()
# 调用：str(对象名)
# __getitem__()
# 调用：对象名[key] or 对象名[start:end:sept]
# 接受类型不同
# __setitem__()
# 调用：对象名[key] = value
# __add__()  和
class My_Test:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s--%d"%(self.name,self.age)

    def __getitem__(self, item):
        if "name" == item:
            return self.name
        if "age" == item:
            return self.age
        else:
            return item

    def __setitem__(self, key, value):
        print("key:%s---value:%s"%(key,value))

    def __add__(self, other):
        print(self.age + other.age)

t1 = My_Test("小梁",39)
t2 = My_Test("小吴",46)
print(t1)                   # __str__
print(t1["name"])           # __getitem__
t1[12] = "武器"             #__setitem__
t1 + t2                     # __add__
print(t1.__dict__)
