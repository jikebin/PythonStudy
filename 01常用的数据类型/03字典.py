'''
1、字典（dict）是以 key : value 形式存储数据的数据类型
2、字典的 key 只能是 不可变类型
3、不可变类型有：数字、字符串、元组
4、可变数据类型有：列表、字典 。。。
5、字典的常见操作：增、删、改、查、遍历
6、注意：字典中每个键值对的存储是没有顺序的，所以不能够使用 切片 进行查找
'''
dic = {"一":"斗","二":"瑞",3:"咪",4:"发",5:"嗖",6:"啦",7:"西"}

# 添加 和 修改 setdefault 、 upadte
# dic[1] = "添加"                   # 没有 key = 1 则添加
# dic[3] = "修改"                   # 有 key = 3  则修改
# dic.setdefault(8,"添加")          # 只能添加,如果存在该key值则什么都不做
# dic.update({4:"替换",9:"添加"})   # 如果存在相同的 key 则将值替换，没有相同的 key 则添加

#删除del、pop、clear、popitem
# del dic[1]                        # 删除 key = 1 的 key:value 对
# dic.pop(3)                        # 弹出 key = 3 的 key:value 对
# dic.clear()                       # 清空字典内容
# dic.popitem()                     # 随机删除一个 key:value 对    

#查询：keys、values、items
# print(dic[1])                     # 查找 key = 1 的 value,如果没有找到，则报错
# print(dic.keys())                 # 查找所有的 key,返回值为 list 类型
# print(dic.values())               # 查找所有的 value,返回值为 list 类型
# print(dic.items())                # 查找说有的 key:value 对，返回值为 [(),()...] 形式

#遍历
# for key in dic:                   # 根据 key 找 value
#     print(key,"---",dic[key])

# for i in dic.values():            # 遍历所有的 value
#     print(i)

# for i in dic.keys():              # 遍历所有的 key
#     print(i)

# for i in dic.items():             # 遍历说有的键值对，元组形式：(key,value)
#     print(i)


