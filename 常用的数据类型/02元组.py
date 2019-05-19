'''
1、元组(tuple) 可以理解成一个只读的 list
2、元组 数据类型在初始化后就不能进行修改
3、常用方法：查找、统计
'''
tup = (3,2,5,4,6)     # 定义元组

# 查找 切片、index(根据值找索引)
print(tup[1:4:1])     # 切片查找,步长为：1(其实不加也行，默认步长就是1)
print(tup.index(5))   # 查找 5 在 tup 中第一次出现的索引数

# 统计 len、count
print(tup.count(5))   # 统计 5 在 tup 中出现的次数
print(len(tup))       # 统计 tup 的长度