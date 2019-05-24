'''
#模块：logging
大纲：日志的五个级别、创建日志的两种方式、配置文件参数说明
日志的五个级别：
    critical(严重的) > error(错误)  > warning(警告) > info(通知信息) > debug(排除故障)
创建日志的两种方式：
    方式1：
        logging.basicConfig(level,format,datefmt,filename,filemode)
        logging.critical("日志信息")
    方式2：
        logging.getLogger()
        logging.FileHandler()
        logging.StreamHandler()
        logging.Formatter()
配置文件参数说明：
    %(asctime)s  字符串形式的当前时间，默认格式为：2018-11-11 12:12:12,222
    %(filename)s 调用日志输出函数的模块的文件名
    %(lineno)d  语句所在的代码行
    %(levelname)s 文本形式的日志级别
    %(name)s    Logger的名字
    %(message)s 用户输出的消息

'''
import logging
#方式1：
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='test.log',
#                     filemode='w')
# logging.debug("这是debug")
# logging.info("这是info")
# logging.warning("这是warning")
# logging.error("这是error")
# logging.critical("这是critical")  #乱码
#-----------------------------------------------------------------------------
#方式二：
# logger = logging.getLogger()
# fh = logging.FileHandler("test.log")
# sh = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fh.setFormatter(formatter)
# sh.setFormatter(formatter)

# logger.addHandler(fh)
# logger.addHandler(sh)

# logger.debug("hehe1")
# logger.info("hehe2")
# logger.warning("hh3")
