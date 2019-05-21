#文件操作
'''
文件打开的两种方式
    1.f = open(path,模式,encoding='utf8')
     f.close()
    2. with open(path,模式,encoding='utf8') as f:
            pass
------------------------------------------------------
模式讲解：
    r 只读                    r+ 可读写
    w 先清空，再写入           w+ 可读写
    a 追加写入                a+ 可读写
    rb  wb  ab   --->以字节的形式进行读或者写操作(重点)用于对多媒体文件进行相关操作
------------------------------------------------------------
常用方法：读、写、光标、刷新、截断、关闭
读： read readline readlines 遍历读取(迭代器)
写： write writelines
光标：tell seek
刷新：flush
截断：truncate
关闭 close
'''
#写操作练习 和 刷新练习 write writelines flush
# with open("test","a+",encoding='utf8') as f:
#     f.write("12324432")
#     f.flush()
#     f.writelines(["a","b","c"])
#     f.writelines(["4","5","6"])

#读操作练习 和 光标练习 read readline readlines tell seek 循环遍历
# f = open("test","r+",encoding="utf8")
# print(f.tell())       # 光标是按照字节数计算，utf-8编码中文占三个字节
# print(f.read(3))      # 从光标处开始读三个字符
# print(f.tell())
# print(f.readline())   # 从光标处开始读
# print(f.tell())
# print(f.readlines())  # 从光标出开始读
# print(f.tell())
# f.seek(20)            # 将光标移动到20位置
# print(f.read())       # 从光标处读取之后的所有文件内容
# for i in f:
#     print(i.strip())
# f.close()
#----------------------------------------------
#截断练习 truncate
# f.truncate(10) #截取前10个字符，将后面内容全部删除，并且将光标移动到该部分

