'''
多线程网络通信：socketserver
大纲：socketserver模块的作用、使用模块的四个步骤、实例
--------------------------------------------------------------------------------------------------------------------
socketserver模块的作用：
    socketserver模块是对socket模块的在封装，里面加入了多线程，方便使用
--------------------------------------------------------------------------------------------------------------------
使用模块的四个步骤：
    1.创建类，继承socketserver.BaseRequestHandler             request:请求  response:响应
    2.重写handle()方法
    3.创建对象，socketserver.ThreadingTCPServer()
    4.通过对象，调用：server_forever()
--------------------------------------------------------------------------------------------------------------------
import socketserver

#调用socketserver练习
class MyServer(socketserver.BaseRequestHandler):

    #重新handle方法
    def handle(self):
        while 1:
            #接收信息（request 中存储数据的通道）
            client_sk = self.request
            data = client_sk.recv(1024)
            print(str(data,"utf8"))
            client_sk.send(data)


#注意：该测试在类外，而不是在类内，注意缩进
if __name__ == '__main__':
    #建立多线程服务端
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8111),MyServer)
    #调用handle()方法,启动程序
    server.serve_forever()
'''