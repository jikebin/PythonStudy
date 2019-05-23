'''
单例模式：
大纲：定义、思想、实现、应用场景
定义：
    单个实例(对象)，只能创建一个对象，永远使用一个对象。
思想：
    1.两个关键成员：
        静态私有成员字段：用于存储类的对象
        类方法：用于创建类对象
    2.调用方式：
        外部不能直接调用构造方法创建对象
        只能通过类方法创建对象
应用场景：
    数据库连接池就是单例模式
实现：
class Demo:
    __sing = None

    @classmethod
    def get_Demo(cls):
        if cls.__sing:
           return cls.__sing
        else:
            cls.__sing = Demo()
            return cls.__sing

print(Demo.get_Demo())
print(Demo.get_Demo())
print(Demo.get_Demo())
'''
class Demo:
    __sing = None

    @classmethod
    def get_Demo(cls):
        if cls.__sing:
           return cls.__sing
        else:
            cls.__sing = Demo()
            return cls.__sing

print(Demo.get_Demo())
print(Demo.get_Demo())
print(Demo.get_Demo())
print(Demo())