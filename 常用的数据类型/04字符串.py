# 支持切片查找的数据类型：列表、元组、字符串
'''
字符串关键知识点：
1.查找：find、切片
2.拼接：join、center、+（不推荐使用）
3.格式化：format、%s、format_map
4.分割：split
5.替换：replace
6.删空格：strip
7.编码：encode、decode
8.统计：count、len
9.大小写：upper、lower
10.判断：in、startswith、endswith
11.eval()
'''

# 查找：find、切片
# string = "sfsfslfnflcclmlkjl"
# print(string[1:5])          # 注意：切片操作，包左不包又
# print(string.find("cc"))    # 查找 cc 在字符串中第一次出现的位置

#拼接 join、center
# s1 = "前一个"
# s2 = "后一个"
# print("/".join([s1,s2]))    # 通过 / 将字符串 s1 和 s2 拼接到一起
# print(s1.center(30,"*"))    # 在 s1 左右两边拼接 15 个 * 让 s1 居中

#格式化 %s、format、format_map
# s1 = '''
#     姓名：{name}
#     年龄：{age}
# '''
# s2 = "我叫 %s 今年 %d 岁!" % ('小明', 10)
# print(s1.format(name="吉祥",age="24"))              # 以 key=value 形式格式化
# print(s1.format_map({"name":"吉祥","age":24}))      # 以 字典 形式格式化
# print(s2)                                           # 通过 %s 和 %d 格式化

#拆分：split
# s1 = "1,2,3,4,5"
# print(s1.split(","))      # 通过 "," 将字符串拆分成列表，注意：每个列表中的数字还是 str 类型

#替换：replace
# s1 = "凉凉的风啊"
# print(s1.replace("凉凉","温暖"))    # 将凉凉替换成温暖

#删空格：strip
# s1 = "   你  是  谁            "
# print(s1.strip())     # 删除 你是谁 两端的空格，注意：中间部分的空格不会被删除

#编码：encode、decode
# s1 = "你是。。。"
# s2 = s1.encode("utf-8")
# s3 = s2.decode("utf-8")
# print(s2)   # b'\xe4\xbd\xa0\xe6\x98\xaf\xe3\x80\x82\xe3\x80\x82\xe3\x80\x82' 
# print(s3)   # 你是。。。

#统计：count、len
# s1 = "    是    啥     "
# print(s1.count(" "))   # 统计空白字符的数量
# print(len(s1))         # 统计 s1 的长度，注意：这里的一个中文字符算一个长度

#大小写：upper、lower
# s1 = "sdfsfsAAAAnk"
# print(s1.upper())     # 全部大写
# print(s1.lower())     # 全部小写

#判断 in、startswith、endswith
# s1 = "第一百零八章"
# print(s1.startswith("第"))  # 判断开头是否相同
# print(s1.endswith("章"))    # 判断结尾是否相同
# print("第" in s1)           # 判断是否包含

#-------------------------------------------------------

# eval()用法一：数据类型的转换
'''
字符串之间的转换：
    str <---> bytes     编码与解码
    str <---> list      eval()与str()
    str <---> tuple     eval()与str()
    str <---> dict      eval()与str()
'''
# li = [1,2,3,4]
# s1 = str(li)    #列表 转字符串
# li1 = eval(s1)  #字符串 转 列表

# eval() 的第二个用法，计算字符串公式
# operator = "(1+3)*3/(1+2)+20/2"
# print(eval(operator))   # 14.0
