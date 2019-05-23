'''
说明：多个函数中有相同参数是，则使用面向对象的编程方式组织内容
基本结构1：
class 类名:
  def __init__(self,参数):
    self._私有参数 = 参数
  def 方法名(self):
    pass
基本结构2： +静态字段
  静态字段特点1：字段内容被所有对象共享
  静态字段特点2：可以用类名.字段名方式直接调用
  静态字段特点3：必须初始化数据
class 类名：
  静态字段名 = 初始化
  def __init__(self):
    pass
  def 方法名(self):
    pass
------------------------------------------------
继承：
  1.python 为多继承
  2.继承顺序为：从左到右，深度继承，如果两个父类有同一个根，则最后继承根。
  3.方法重写后，调用父类方法的两种方式：
    方式1：super(子类名,self).function(参数...)
    方式2：父类名.function(self,参数...)
------------------------------------------------
类成员：
  字段：
    普通字段：函数内
    静态字段：类内，函数外
  方法：
    普通方法：+self参数
    构造方法：__init__(self,...)
    静态方法：@staticmethod,self参数不是必须的
    类方法：@classmethod，将self参数改成 cls; cls 代表类名，而不是对象名；类方法是特殊的静态方法
  属性/特性：
    方式1：
      @property           get操作
      @属性名.setter      set操作
      @属性名.deleter     del操作
    方式2：
      属性名 = property(fget=函数名1,fset=函数名2,fdel=函数名3)
    调用：
      value = 对象名.属性名   # 调用get操作
      对象名.属性名 = value   # 调用set操作
      del 对象名.属性名       # 调用del操作
'''
class Student:
  # 定义静态字段
  my_class = "一年E班"
  # 定义构造方法,python中 __代表私有
  def __init__(self,name="小米",age=21,sex="女")：
    self.__name = name
    self.__age = age
    self.__sex = sex
  def setName(self,name):
    self.__name = name
  def getName(self):
    return self.name
  def getName(self):
    return self.__name
  def setAge(self,age):
    self.__age = age
  def getAge(self):
    return self.__age
  def getSex(self):
    return self.__sex
  def show(self):
    print("name:%s,age:%d,sex:%s"%(self.__name,self.__age,self.__sex))
  def show_cls(self):
    print(self.my_class)  
# 小明 继承 Student
class xiaoming(Student):
  def show(self):
    # super(xiaoming,self).show()
    Student.show(self)
# s1 = xiaoming()
# s1.show()
# stu1 = Student()
# stu2 = Student()
#
# # stu.show()
# # stu.setAge(11)
# # stu.setName("小花")
# # stu.show()
# # print(stu.__name)
# Student.my_class = "name"
# print(Student.my_class)
# print(stu1.my_class)
# print(stu2.my_class)
#---------------------------------------------------------------------------------------------------------------
class Test:
  def __init__(self,name="叶修"):
    self.__name = name
    print("构造方法")
  # @property
  # def name(self):
  #   return self.__name
  # @name.setter
  # def name(self,name):
  #   self.__name = name
  def get(self):
    return self.__name
  def set(self,name):
    self.__name = name
  name = property(get,set)
t1 = Test()
print(t1.name)
t1.name = "苏沐橙"
print(t1.name)