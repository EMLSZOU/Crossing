# Django学习

## 底层Socket套接字

一个框架：处理Socket，MVC（Model-View-Control），多线程（Threading），然后提供接口（函数或类）

Socket是操作系统的系统调用API。很多编程语言都可以调用Socket。

网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。
建立网络通信连接至少要一对端口号(socket)。socket本质是编程接口(API)对TCP/IP的封装，TCP/IP也要提供可供程序员做网络开发所用的接口，这就是Socket编程接口。
Socket的英文原义是“孔”或“插座”，通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机之间的通信。

socket是进程间通信的一种方法 (参考Linux进程间通信)，它是基于网络传输协议的接口（传输层）。TCP socket与双向管道(duplex PIPE)有些类似，一个进程向socket的一端写入或读取文本流，而另一个进程可以从socket的另一端读取或写入，比较特别是，这两个建立socket通信的进程可以分别属于两台不同的计算机。所谓的TCP协议，就是规定了一些通信的守则，以便在网络环境下能够有效实现上述进程间通信过程。双向管道(duplex PIPE)存活于同一台电脑中，所以不必区分两个进程的所在计算机的地址，而socket必须包含有地址信息，以便实现网络通信。一个socket包含四个地址信息: 两台计算机的IP地址和两个进程所使用的端口(port)。IP地址用于定位计算机，而port用于定位进程 (一台计算机上可以有多个进程分别使用不同的端口)。

socket有许多种类型，比如基于TCP协议或者UDP协议(两种网络传输协议)。其中又以TCP socket最为常用。

#### TCP Socket

服务器开放自己的端口，被动等待其他计算机连接。客户机主动使用socket连接到服务器的时候，服务器就开始为客户提供服务。

`host.py` ：服务器端，使用bind()方法来赋予socket以固定的地址和端口，并使用listen()方法来被动的监听该端口。当有客户尝试用connect()方法连接的时候，服务器使用accept()接受连接，从而建立一个连接的socket。

```python
import socket
# 创建一个socket对象，指定IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)
host_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_skt.bind(('127.0.0.1', 8008))  # ip、端口号组成的元组。ip可为 ''
host_skt.listen(3)  # 最大的连接数
conn, addr = host_skt.accept()  # 接受请求，并且建立连接
request = conn.recv(1024)  # 接收数据（指定缓冲量）
print('Connected by: %s  request: %s' % (addr, request.decode('utf8')))
conn.sendall('Connected. Bye.'.encode('utf8'))  # 回复信息
conn.close()  # 关闭连接
```

`client.py` ：客户端，用connect()方法连接服务器，之后用

```python
import socket
client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_skt.connect(('127.0.0.1', 8008))  # ip、端口号组成的元组
client_skt.send('From Client: Can you hear me?'.encode('utf8'))  # 发送信息
reply = client_skt.recv(1024)
print('reply: %s' % reply.decode('utf8'))
client_skt.close()
```

#### 基于TCP socket的HTTP服务器

上面已经用 TCP socket 建立了两台远程计算机的连接。然而，socket传输自由度太高，有安全和兼容的问题。所以，应用层的协议(比如HTTP协议)来规定socket使用规则，以及所传输信息的格式。

HTTP协议利用请求-回应(request-response)的方式来使用TCP socket。客户端向服务器发一段文本作为request，服务器端在接收到request之后，向客户端发送一段文本作为response。在完成了这样一次request-response交易之后，TCP socket被废弃。下次的request将建立新的socket。

`httpd.py`：构建一个http服务器。HTTP response分为起始行(start line), 头信息(head)、空行 和主体(body)

- 起始行：HTTP/1.x 版本号 200 状态码 OK 状态码
- 头信息： Content-Type 响应内容
- 主体： 响应的内容。HTML网页、图像、视频…

```python
import socket
# 建立 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
# 组建 文本 HTTP 响应报文。编码为二进制数据
text_content = '''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''
text_content = text_content.encode('utf8')  # utf-8字符串编码为二进制
# 组建 图片 HTTP 响应报文。编码为二进制数据
f = open('test.jpg', 'rb')
pic_content = '''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content = pic_content.encode('utf-8') + f.read()  # 字符串和图片都变为二进制流
f.close()
# 启动服务器
while 1:  # 死循环，不停歇的服务器
    # 3: maximum number of requests waiting
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    request = conn.recv(1024)
    print('Request is:', request)
    method = request.decode('utf8').split(' ')[0]
    src = request.decode('utf8').split(' ')[1]
    # deal with GET method
    if method == 'GET':
        if src != '/test.jpg':
            content = text_content
        else:
            content = pic_content
        conn.send(content)
    conn.close()
```

如果要写 HTTP 客户端，请求报文request也分分为起始行(start line), 头信息(head)、空行 和主体(body)

- 起始行：GET 请求方法，/test.jpg 网址，HTTP/1.x 版本号
- 头信息： 很多。
- 主体： GET方法没有。POST方法有主体。

运行`httpd.py`，浏览器打开 http://localhost:8000/ 就会看到服务器的响应内容。而服务器接收到的请求报文如下：

```XML
Connected by ('127.0.0.1', 62146) 浏览器第一次请求网页。服务器给它回复HTML文本。
Request is: b'GET / HTTP/1.1\r\n
Host: localhost:8000\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: zh-CN,zh;q=0.8\r\n\r\n'

Connected by ('127.0.0.1', 62147) 浏览器发现HTML含有IMG图片，再次请求。服务器回复图片
Request is: b'GET /test.jpg HTTP/1.1\r\n
Host: localhost:8000\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36\r\nAccept: image/webp,image/*,*/*;q=0.8\r\nReferer: http://localhost:8000/\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: zh-CN,zh;q=0.8\r\n\r\n'
```

可改进的地方：

- while循环实现不停歇的服务器。这里可以引入多进程、多线程。
- 服务器能提供的功能很少。与数据库、NTP等交互可以提供更多服务。
- 理解了socket包，就能利用socketserver等更高级的包快速开发。

