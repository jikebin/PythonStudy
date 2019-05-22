'''
模块：time 和 datetime
大纲：时间展示、时间格式转换、睡眠
时间展示：time() gmtime() localtime() ctime()
    时间戳：time()
    结构化：localtime()
    字符串：ctime()  和   datetime.datetime.now()
时间格式转换：
    结构化转自定义字符串：  strftime()
    自定义字符串转结构化：  strptime()
    结构化转时间戳：        mktime()
    时间戳转结构化：        localtime()
    时间戳转字符串：        ctime()
    注意：字符串没有办法直接转换成时间戳，需要借助结构化时间格式
睡眠：
    sleep()
-------------------------------------------------------------------------------------------
'''
import time
import datetime
#时间展示：
# print(time.time()) #时间戳：1548475610.2778366
# print(time.localtime())#格式化：time.struct_time(tm_year=2019, tm_mon=1, tm_mday=26, tm_hour=12, tm_min=6, tm_sec=50, tm_wday=5, tm_yday=26, tm_isdst=0)
# print(time.ctime()) #字符串：Sat Jan 26 12:06:50 2019
# print(datetime.datetime.now()) #字符串：2019-01-26 12:06:50.277836
#时间格式转换：
time1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) #结构化转自定义字符串格式
print(time1) #2019-01-26 12:12:18
time2 = time.strptime(time1,"%Y-%m-%d %H:%M:%S") #自定义字符串格式转结构化
print(time2) #time.struct_time(tm_year=2019, tm_mon=1, tm_mday=26, tm_hour=12, tm_min=12, tm_sec=18, tm_wday=5, tm_yday=26, tm_isdst=-1)
#----------------------
time3 = time.mktime(time2) # 结构化转时间戳
print(time3)
time4 = time.localtime(3600)# 时间戳转结构化
print(time4)
#-------------------------
time5 = time.ctime(3600) # 时间戳转字符串
print(time5)