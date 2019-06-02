'''
网络通信：服务器端
'''
# import socket
# server_sk = socket.socket()   # 默认参数为：family=AF_INET,type=SOCK_STREAM
# #定义服务器IP地址和端口号
# add = ("127.0.0.1",8011)
# #绑定IP和端口
# server_sk.bind(add)
# # address = ("127.0.0.1",8011)# 注意：端口号是int类型，如果写成str类型，则会报错
# # server_sk.bind(address)
# #设置最大监听数量
# server_sk.listen(2)
# #等待阻塞
# print("等待客户端连接... ...")
# client_sk,client_address = server_sk.accept()
# client_sk.send("连接成功".encode("utf8"))
# print(str(client_sk.recv(1024),"utf8"))
#---------------------------------------------------------------------------------------------------------------------
'''
多线程网络通信：socketserver
该模块是面向对象的
'''
#多线程网络通信：服务器端
import socketserver

class MySocket(socketserver.BaseRequestHandler):

    def handle(self):
        client_sk = self.request
        client_sk.send(bytes("连接成功","utf8"))
        while True:
            #定义回传信息
            date = client_sk.recv(1024)
            client_sk.send(date)
#创建多线程对象
server_obj = socketserver.ThreadingTCPServer(("127.0.0.1",8011),MySocket)
server_obj.serve_forever()
