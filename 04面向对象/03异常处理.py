'''
异常处理：
大纲：异常处理基本结构、主动触发异常、断言、自定义异常
异常处理的基本结构：
    try:
        print("正常执行代码")
    except: Exception as e:
        print("出错执行部分：",e)
    else:
        print("如果不出错，则执行该部分")
    finally:
        print("最后执行该部分")
主动触发异常：raise
    raise Exception("出错了哟。。。")
断言：assert
    特点：用于强制用户服从，不服从就报错，可捕获，一般不捕获
    assert 条件表达式        #条件成立则通过，不成立则报错
自定义异常：继承Exception
class MyExcept(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
--------------------------------------------------------------------------------------------------------------------
'''
class MyExcept(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    #raise MyExcept("强制触发异常...")
    assert 1 == 1        #定制断言

except MyExcept as e:
    print(e)
except Exception as e:
    print("捕获所有其他异常...")
else:
    print("不触发异常则执行该代码块")
finally:
    print("最后执行finally代码块")

