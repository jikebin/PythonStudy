'''
模块：json/pickle
大纲：两个函数、json和pickle的区别
两个函数：
    dumps()  其他类型 ---> json类型
    loads()  json类型 ---> 其他类型
json和pickle的区别：
    1.json是字符串类型数据，pickle是bytes类型数据
    2.json只能存储基本的数据类型，pickle可以存储函数类型
'''
import json,pickle
list1 = [1,2,3,4,4]
dict1 = {"key1":"value1"}
# date1= json.dumps(list1)
# date2 = json.dumps(dict1)
# print(type(date1),type(date2))
# with open("json.txt","w") as f:
#     f.write(date1)
#     f.write("\n")
#     f.write(date2)
#读操作
# f = open("json.txt","r")
# date1 = f.readline()
# date2 = f.readline()
# list2 = json.loads(date1)
# dict2 = json.loads(date2)
# print(type(list2),type(dict2))
#----------------------------------------------------------
date1 = pickle.dumps(list1)
date2 = pickle.dumps(dict1)
# print(date1,date2)
# print(type(date1),type(date2))
# with open("pickle.txt","wb") as f:
#     f.write(date1)
f = open("pickle.txt","rb")
value = pickle.loads(f.read())
print(value)