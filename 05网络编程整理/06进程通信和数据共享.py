'''
进程通信和数据共享：
大纲：进程的两种创建方式(multiprocessing.Process)、进程通信(进程队列和pipe)、数据共享(Manger)
----------------------------------------------------------------------------------------------------------------------
进程的两种创建方式：
from multiprocessing import Process
    面向过程:
        p1 = Process(target=function,args=(参数,))
        p1.start()
    面向对象：
        1.创建对象，并继承：Process
        2.子类构造，调用父类构造
        3.重写run()方法
        4.创建对象
        5.调用start()方法，启动进程
        注意：创建对象，必须在  if __name__ == '__main__': 下完成，否则报错
----------------------------------------------------------------------------------------------------------------------
进程通信：Queue、pipe
    进程通信：一般是主进程和子进程之间的通信。
    通信方式1：Queue
        from multiprocessing import Queue
        1.在主进程中创建：Queue()对象
        2.将对象传进子进程方法中
        3.使用该方法，调用put() 或 get()对象
        4.在主进程中调用：put() 或 get()对象,即可实现线程之间的通信
        原理：Queue()内部，通过pickle方法，实现进程之间的数据通信
    通信方式2：Pipe 管道
        from multiprocess import Pipe
        1.parent_conn,child_conn = Pipe()  # 获取子进程和主进程的管道
        2.将child_conn 传入到子进程
        3.通过：recv() 和 send() 进行数据通信
        原理：通过使用网络通信，在实现进程之间的通信
        注意：recv()不能有参数，send()是str类型参数

----------------------------------------------------------------------------------------------------------------------
数据共享：Manager
from multiprocessing import Manager
核心程序：
    with Manager as manager:
        d = manager.dict()
        l = manager.list()
实例：
def public(list1,dict1,n):
    dict1[n] = n
    list1.append(n)

if __name__ == '__main__':
    with Manager() as manage:
        l = manage.list()
        d = manage.dict()
        p_list = []

        for i in range(10):
            p = Process(target=public,args=(l,d,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(l)
        print(d)
----------------------------------------------------------------------------------------------------------------------
'''
# 进程通信
from multiprocessing import Process,Queue,Manager
import os,time
# def demo(name):
#     print("进程号为：",os.getpid())
#     time.sleep(1)
#     print(name)
# if __name__ == '__main__':
#     print("start")
#     p1 = Process(target=demo,args=("进程1",))
#     p2 = Process(target=demo,args=("进程2",))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("end")
# class TestPro(Process):
#     def __init__(self,q):
#         Process.__init__(self)
#         self.q = q

#     def run(self):
#         print("Test")
#         self.q.put("你好")

# #创建进程
# if __name__ == '__main__':
#     queue1 = Queue()

#     p = TestPro(queue1)
#     p.start()
#     print(queue1.get())
#-----------------------------------------------------------------------------------------------------------------
def public(list1,dict1,n):
    dict1[n] = n
    list1.append(n)

if __name__ == '__main__':
    with Manager() as manage:
        l = manage.list()
        d = manage.dict()
        p_list = []

        for i in range(10):
            p = Process(target=public,args=(l,d,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(l)
        print(d)