'''
队列：
大纲：队列的用途、队列的种类、队列的基本实现
--------------------------------------------------------------------------------------------------------------------
队列的用途：
队列是多线程的利器，保证数据的安全性
多线程操作列表的过程中，会出现线程不安全。而多线程操作队列数据，则安全，队列内本身有一把锁
--------------------------------------------------------------------------------------------------------------------
队列的种类：
    1.FIFO：先进先出
    2.LIFO：后进先出
    3.按照优先级
--------------------------------------------------------------------------------------------------------------------
队列的基本实现：
import queue
d = queue.Queue(3)    #队列内数据的个数
d.put("数据")         #插入数据
d.get()               #取出数据
--------------------------------------------------------------------------------------------------------------------
'''