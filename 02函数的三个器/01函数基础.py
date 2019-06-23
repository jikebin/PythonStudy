'''
基础大纲：
  函数特点、参数定义、参数赋值、函数返回值、变量作用域、高阶函数、递归思想
函数特点：
  1、减少重复代码
  2、易于修改和扩展
  3、保持代码的一致性
参数定义：
  1、关键参数：name,age
  2、默认值参数：age = 12
  3、无命名可变长参数：*args
  4、有命名可变长参数：**args
  参数定义顺序：关键参数 > 默认值参数 > 无命名可变长参数 > 命名可变长参数
参数赋值：
  1、顺序赋值       function(参数1,参数2...)
  2、键值对形式赋值：function(形参1=实参1,形参2=实参2......)
  3、无命名可变长参数统一赋值：function(*[1,2,3,4])
  4、有命名可变长参数统一赋值：func(**{key:value,key:value})
函数的返回值：
  1.默认返回值  return None
  2.一个返回值  return value
  3.多返回值  return v1,v2,v3 ...
  注意1：python函数支持多返回值，会将多个返回值封装成元组显示
变量作用域：LEGB
  说明：python变量的作用域是以函数为最小单位的。而其他语言是以{}为最小单位
    L: local        （嵌套作用域） 例：嵌套函数里边的变量
    E: enclosing    （内部作用域） 例：函数中的变量
    G: global        (全局作用域)  例：在文件最外层的变量
    B: built-in     （系统作用域） 例：int() str()
  补充1：内部作用域中，修改全局作用域：global 变量名
  补充2：嵌套作用域中，修改内部作用域：nonlocal 变量名
高阶函数特性：
  函数可以作为参数和返回值
递归函数：
  1.有入口有出口
  2.自己调用自己
  3.所有递归都可以使用循环来替代
'''
# 关键参数和默认值参数使用，如下：
def func(name,age=13):
    print("name=%s"%name)
    print("age=%d"%age)
# func("小明")    # 关键参数必须赋值，默认自参数可选

# 无命名可变长参数使用，如下：
def fun1(*args):
    print("args=",args)
    for value in args:  # args 是元组形式
        print(value)
# fun1([1,2,3,4])       # args= ([1, 2, 3, 4],)
# fun1(*[1,2,3,4])      # args= (1, 2, 3, 4)
# 补充：传入[1,2,3,4] *args 会将其当成一个参数进行获取，而传入*[1,2,3,4] 则 *args 会将其当成4个参数进行获取

# 有命名可变长参数使用，如下：
def fun2(**kwargs):
    print("kwargs = ",kwargs)
    for key in kwargs:
        print("key=%s --- value=%s"%(key,kwargs[key]))
fun2({"a":"A","b":"B"})   # 报错
fun2(key1=1,key2=2)       # kwargs =  {'key2': 2, 'key1': 1}
fun2(**{"a":"A","b":"B"}) # kwargs =  {'b': 'B', 'a': 'A'}

# 在内部作用域中，修改全局作用域内容
count = 10
def show():
    global count
    count+=1
show()
print("count=%s"%count) # count=11