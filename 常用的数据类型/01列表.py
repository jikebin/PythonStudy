'''
更多详细内容可以找 w3cschool : https://www.w3cschool.cn/python/dict

1、python 中的列表 list 相当于其他语言的数组
2、区别是 list 的长度是可变的，而数组的长度是固定的
3、python 中的列表有可以特性是“切片”，这是其他语言没有的（反正我是不知道）
4、list 的常用方法：增加、删除、修改、查询、排序、统计、判断
'''
li = [2,4,5,6,7,2,1,3,1]

# 添加 append、insert、extend
# li.append("end")        # 在末尾添加
# li.insert(0,"first")    # 在索引位置添加
# li.extend([1,2])        # 在结尾添加多个，也可以理解成合并两个 

# 删除 del、pop、remove、clear
# del li[0]               # del 可以用于各种数据的删除，不限于 list
# li.pop(1)               # 默认弹出最后一个元素，也可以指定弹出的 list索引
# li.remove("end")        # 删除 end 值的第一个匹配项
# li.clear()              # 清空 list 内所有数据

# 修改 修改一个、批量修改(通过 切片 进行修改)
# li[0] = "start"         # 修改一个
# li[2:] = [2,3,4]        # 通过切片操作进行修改多个

# 查询 切片(根据索引查值)、index(根据值找索引)
# print(li[2:4])          # 查找从索引 2~4 的所有数据（包左不包右）
# print(li[2:])           # 查找从索引 2到最后的所有数据
# print(li[1:4:2])        # 第二个：后面的叫做步长，也可以理解为间隔（每隔2个取一个值）

# 统计 len、count
# print(len(li))          # len() 可以统计 list、dict、tuple、set 等数据类型长度
# print(li.count("end"))  # 统计指定 value 出现的次数

# 排序 sort 、reverse
# li.sort()               # 默认为从小到大，如果出现了不同数据类型，则会报错
# li.sort(reverse=True)   # 从大到小排序
# li.reverse()            # 倒叙排列

# 判断 is、in 两个关键字
# print(type(li) is list) # 判断 li 是否是 list 数据类型
# print(1 in li)          # 判断 1 是否在 li 列表中

print(li,end = " ")   #补充，print()在 python3中会自动换行，如果不需要自动换行则 print(内容部分 , end = "") 即可

