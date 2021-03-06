'''
网站原理：
	客户端----> 服务端
	发送请求，响应内容
http端口号：80
https端口号：443
ssh端口号：22
redis端口号：6379
mongo端口号：27017

http与https区别？
	1、http是明文传输，不安全
	   https在http基础上加入了 SSL协议，更加安全
	主要区别：
1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用
2、http是超文本传输协议、信息是明文传输，https则是具有安全性SSL加密传输协议
3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443
4、http的连接很简单，是无状态的；https协议是由SSL+HTTP协议构建的可进行加密传输、
身份认证的网络协议、比http协议安全。
-----------------------------------------------------
http响应模型：
	1、请求、相应模型
	缺点：服务器端不能主动推送给浏览器端内容
工作流程：
1、首先客户端和服务器建立连接（TCP连接，三次握手）

2、建立连接后，客户端发送一个请求给服务器，
	请求格式为：URL、协议版本号、后边是MIME信息包括
	请求修饰符、客户机信息和可能的内容。
	
3、服务器接到请求后，给予相应的相应信息，其格式为一个状态行，
	包括信息的协议版本号，一个成功或错误的代码，后边是MIME信息
	包括服务器信息、实体信息和可能的内容。
	
4、客户端接收服务器所返回的信息通过浏览器显示在用户的显示屏上，
	然后客户机与服务器断开连接。
http请求
	一个完整的HTTP请求包括如下内容：一个请求行、若干消息头、以及实体内容
		
http响应：
	响应内容包括：状态行、多个消息头、实体内容
	状态行：
		200：请求成功
		301：永久重定向
		302：临时重定向
		403：禁止访问
		404：没有找到
		500系列是服务器错误
请求头信息要掌握，响应头信息了解即可。		

'''