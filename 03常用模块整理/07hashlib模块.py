'''
#模块：hashlib
大纲：加密说明、加密算法、加密步骤
加密说明：
    1.该加密模块加密后的内容不可解密
    2.用法：存储密码，用户每次输入密码后，都进行加密操作，在与数据库加密内容进行比对验证
加密算法：
    md5     sha256
加密步骤：
    1.m = hashlib.md5() #获取加密算法对象
    2.m.update(bytes类型) #加密数据
    3.value = m.hexdigest() #获取加密后数据
'''
import hashlib
m = hashlib.md5()
#m = hashlib.sha256()
m.update("你好".encode("utf8"))
#print(m.hexdigest())
value = m.hexdigest()
print(value)