'''
模块整理：10个
大纲：time、random、os、sys、
    hashilb、logging、configparser、re
    json、pickle、模块导入
-------------------------------------------------------------------------------------------
模块导入：
大纲：模块导入的三种方式、模块导入的三级结构
三级结构：包 --- 模块  ---- 函数/类
import 模块名
from 模块名   import 函数名
from 包名.模块名  import 函数名
导入导入路径：sys.path.append(...)
-------------------------------------------------------------------------------------------
time模块：datetime模块
大纲：显示时间、时间转换、sleep()
显示时间：
    时间戳：time.time()
    结构化：time.localtime()            time.gmtime()
    字符串：datetime.datetime.now()     time.ctime()
时间转换：
    时间戳--->结构化：localtime(时间戳)
    结构化--->时间戳：mktime(结构化)
    结构化--->字符串：strptime()
    字符串--->结构化：strftime()
    时间戳--->字符串：ctime()
-------------------------------------------------------------------------------------------
random模块：
大纲：数字、序列
数字：
    random()
    randint(1,10)
    randrange(1,10)
序列：
    chioce([])
    sample([],2)
-------------------------------------------------------------------------------------------
os模块：
大纲：文件/文件夹操作，路径操作，os.system(shell)
文件/文件夹操作：
    os.makedirs()   os.mkdir()
    os.removedirs() os.rmdir()
    os.remove() 删除文件和文件夹
    os.sate(path)   获取文件信息
    os.rename()     更改名称
    os.listdir()            #展示文件目录，以元组形式返回
    os.chdir()              #更改当前工作目录路径(默认相对路径的根目录)
路径操作：
    __file__
    os.path.abspath(__file__)
    os.path.dirname()
    os.path.basename()
    os.path.split()
    os.path.join()
    os.getcwd()  #展示当前工作目录(相对目录的绝对路径)
    os.sep      #显示系统路径分隔符


-------------------------------------------------------------------------------------------
hashilb模块：
大纲：加密算法、加密操作
加密类型：
    md5、sha256
加密操作：
m = hashlib.md5()
m.append("加密数据".encode("utf8"))
m.hexdigest()
-------------------------------------------------------------------------------------------
logging模块：
大纲：日志的五个级别
五个级别：
    debug < info < warning <error < critical
-------------------------------------------------------------------------------------------
configparser模块：
大纲：写操作、读操作
写操作：
config = confgigparser.ConfigParser()
config[key] = {字典}
with open(path,"a",encoding="utf8") as f:
    config.write(f)
读操作：
config = confgigparser.ConfigParser()
config.read()
value = config[key]
config.defaults()
config.sections()
-------------------------------------------------------------------------------------------
re模块：
大纲：12个元字符+5个方法
12个元字符：
    匹配字符：
        .       匹配任意一个
        []      集合中匹配一个
        ()      匹配一个元组  (?:) 取消元组优先级
    匹配数量：
        ？
        +
        *
        {}
    其他：
        ^   在[]内表示取反，在[]内表示开头
        $   表示结尾
        |  表示或
        \   取消元字符功能，增加普通字符功能：\d \w \b \s(临界字符)
        -  在[]表示范围 a-z 0-9
    在[]拥有元字符功能的有：-\^
    \\\\匹配一个\
    r"\\" 匹配一个\
5个方法：
    re.sub()
    re.findall()
    re.split()
    re.match()
    re.search()
    re.compile()                        #将正则表达式封装成对象，然后通过该对象调用上面的5个方法
---------------------------------------------------------------------------------------------------------------------
json/pickle模块
大纲：两个方法、json和pickle的区别
两个方法：
    json --> 其他：loads()
    其他 --> json dumps()
json和pickle的区别：
    1.json是字符串类型数据，pickle是bytes类型数据
    2.json只能存储基本的数据类型，pickle可以存储函数类型

---------------------------------------------------------------------------------------------------------------------
遗忘内容：
    os模块：
        os.listdir()
        os.chdir()
        os.getcwd()
        os.sep
    hashlib模块：
        m.update(bytes类型)
    configparser模块：
        读操作：config.sections()
    re模块：
        \s  空白字符匹配
        re.compile()                        #将正则表达式封装成对象，然后通过该对象调用上面的5个方法
    json/pickle模块：
        json和pickle的区别：
            1.json是字符串类型数据，pickle是bytes类型数据
            2.json只能存储基本的数据类型，pickle可以存储函数类型

---------------------------------------------------------------------------------------------------------------------
'''
import time,datetime,random,os,hashlib,logging,re
re.sub()
re.findall()
re.split()
re.match()
re.search()

# logging.critical()
# m = hashlib.sha256()
# m.update(bytes("你好","utf8"))
# print(m.hexdigest())
# print(os.stat("模块复习1.py"))
# random.choice([x for x in range(10)])
# s = random.sample([x for x in range(10)],2)
# print(s)
#os.path.dirname()
# print(datetime.datetime.now())
# print(time.ctime())