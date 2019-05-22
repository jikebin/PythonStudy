'''
模块：configparser
大纲：模块的写操作、模块的读操作
模块的写操作：
config = configparser.ConfigParser()
config["key"] = {"key1":"value"}
with open("test.ini","w",encoding="utf8") as f:
    config.write(f)
模块的读操作：
    1.创建config对象： config = configparser.ConfigParser()
    2.加载配置文件： config.read("文件名")
    3.读取操作：config["key1"]["key1"]
    4.其他方法：sections()  defaults()

'''
import configparser
config = configparser.ConfigParser()
#配置文件模块的写操作
# config["DEFAULT"] = {"key1":"value1"}
# config["url"] = {"baidu":"www.baidu.com","jingdong":"www.jd.com","360":"www.360.com"}
# config["info"] = {"baidu":"best big WWW"}
# with open("test.ini","w",encoding="utf8") as f:
#     config.write(f)
#配置文件的读操作
config.read("test.ini") #该方法是将test.ini文件信息加载到config对象中
print(config["url"])
for i in config["url"]:
    print(i)
t1 = config.sections()
print(t1)
d1 = config.defaults()
print(d1)