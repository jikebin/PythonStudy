'''
网络通信：客户端
'''
import socket
client_sk = socket.socket()
address = ("127.0.0.1",8011)
#连接服务器
client_sk.connect(address)
print(client_sk.recv(1024).decode("utf8"))
while True:
    date = input(">>>")
    client_sk.send(bytes(date,"utf8"))
    print(client_sk.recv(1024).decode("utf8"))