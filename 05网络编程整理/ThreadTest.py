'''
多线程创建练习：
多线程操作：是为了增加程序的执行效率，python操作，只能增加IO密集型操作
'''
#面向过程操作
import threading,time
def thread1(name):
    print("看电影:",name)
    time.sleep(5)
def thread2(name):
    print("听音乐:",name)
    time.sleep(3)
#开启两个线程，分别用于听歌和看电影
start = time.time()
t1 = threading.Thread(target=thread1,args=("流浪地球",))
t1.start()
t2 = threading.Thread(target=thread2,args=("稻香",))
t2.start()
t1.join()
t2.join()
end = time.time()
print(end - start)
