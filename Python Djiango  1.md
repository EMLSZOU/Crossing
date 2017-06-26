## 底层：Socket套接字、HTTP报文

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
<body>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</body>
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


#### 支持POST方法的服务器

增添表格，以及处理表格提交数据的"POST"方法。

```python
import socket
# 建立 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
# 这里增加了表格
text_content = '''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<body>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="Submit">
</form>
</body>
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
while 1:
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
    if method == 'POST': # 处理 POST
        form = request.decode('utf8').split('\r\n')
        idx = form.index('')
        entry = form[idx:]
        value = entry[-1].split('=')[-1].encode('utf-8')
        conn.send(text_content + '\n <p>'.encode('utf-8') + 
                  value + '</p>'.encode('utf-8'))
    conn.close()
```

服务器进行的操作很简单，即从POST请求中提取数据，再显示在屏幕上。

#### 用socketserver简化socket的使用

上面使用socket，必须先设置socket的类型，然后依次调用bind(),listen(),accept()，最后使用while循环来让服务器不断的接受请求。用socketserver可以简化这个流程。

```python
import socketserver
from http.server import HTTPServer
class TCPhandler(socketserver.BaseRequestHandler):
    # 改写handler()方法，来具体规定不同情况下服务器的操作
    def handle(self):
        # 组建 文本 HTTP 响应报文。编码为二进制数据
        text_content = '''HTTP/1.x 200 OK
        Content-Type: text/html

        <head>
        <title>WOW</title>
        </head>
        <body>
        <p>Wow, Python Server</p>
        <IMG src="test.jpg"/>
        <form name="input" action="/" method="post">
        First name:<input type="text" name="firstname"><br>
        <input type="submit" value="Submit">
        </form>
        </body>
        '''
        text_content = text_content.encode('utf8')  # utf-8字符串编码为二进制
        # 组建 图片 HTTP 响应报文。编码为二进制数据
        f = open('test.jpg', 'rb')
        pic_content = '''HTTP/1.x 200 OK
        Content-Type: image/jpg

'''# 注意多行字符串 与 HTTP报文格式的问题
        pic_content = pic_content.encode('utf-8') + f.read()  # 字符串和图片都变为二进制流
        f.close()
        # 用self.request读取客户端请求
        request = self.request.recv(1024)
        # 用self.client_address引用客户端的地址
        print('Connected by:', self.client_address[0])
        print('Request is:', request)
        method = request.decode('utf8').split(' ')[0]
        src = request.decode('utf8').split(' ')[1]
        # deal with GET method
        if method == 'GET':
            if src != '/test.jpg':
                content = text_content
            else:
                content = pic_content
            self.request.send(content)
        if method == 'POST':
            form = request.decode('utf8').split('\r\n')
            idx = form.index('')
            entry = form[idx:]
            value = entry[-1].split('=')[-1].encode('utf-8')
            self.request.send(text_content + '\n <p>'.encode('utf-8') + value + '</p>'.encode('utf-8'))
# 用(ip,端口),Handler 建立一个TCPServer的对象，然后用serve_forever()实现不停歇的服务
server = socketserver.TCPServer(('', 8000), TCPhandler)  # Handler类定义如何操作Socket（如何收发报文）
server.serve_forever()  # 让服务器不断工作
```

#### 基于HTTP的服务器

###### SimpleHTTPServer处理GET方法

HTTP协议基于TCP协议，但增加了更多的规范。一个HTTP请求(request)包含有两个重要信息：请求方法和URL。根据请求方法和URL的不同，一个大型的HTTP服务器可以应付成千上万种不同的请求。在Python中，可以使用SimpleHTTPServer包和CGIHTTPServer包来规定针对不同请求的操作。

其中，SimpleHTTPServer可以用于处理GET方法和HEAD方法的请求。它读取request中的URL地址，找到对应的静态文件，分析文件类型，用HTTP协议将文件发送给客户。

```python
# httpsvr.py 文件
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler  # Python3
# from SimpleHTTPServer import SimpleHTTPRequestHandler Python2
server = TCPServer(('', 8000), SimpleHTTPRequestHandler)  # 建立TCPServer的对象
server.serve_forever()  # 让服务器永远运行
```

在当前目录放置一个HTML文件 index.html

```HTML
<html>
<head>
    <title>WOW</title>
</head>
<body>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="/" method="post">
    First name:<input type="text" name="firstname"><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>
```

将内容存放于静态文件 index.html，并根据URL为客户端提供内容，这让内容和服务器逻辑 分离。每次更新内容时，可以只修改静态文件，而不用停止整个Python服务器。

这些改进也付出代价。在原始程序中，request中的URL只具有指导意义，可以在代码中规定任意的操作。在SimpleHTTPServer中，操作与URL的指向密切相关。用自由度，换来了更加简洁的程序。

SimpleHTTPRequestHandler不能处理POST请求。

###### CGIHTTPRequestHandler处理POST请求

CGI (Common Gateway Interface)。CGI是服务器和应用脚本之间的一套接口标准。它的功能是让服务器程序运行脚本程序，将程序的输出作为response发送给客户。总体的效果，是允许服务器动态的生成回复内容，而不必局限于静态文件。

支持CGI的服务器程接收到客户的请求，根据请求中的URL，运行对应的脚本文件。服务器会将HTTP请求的信息和socket信息传递给脚本文件，并等待脚本的输出。脚本的输出封装成合法的HTTP回复，发送给客户。CGI可以充分发挥服务器的可编程性，让服务器变得“更聪明”。

服务器和CGI脚本之间的通信要符合CGI标准。CGI的实现方式有很多，比如说使用Apache服务器与Perl写的CGI脚本，或者Python服务器与shell写的CGI脚本。

CGIHTTPRequestHandler类继承自SimpleHTTPRequestHandler类，所以可以像父类一样处理GET方法和HEAD方法的请求，提供静态文件的服务。此外还可以用来运行CGI脚本。如果URL指向静态文件，服务器就将文件的内容传送到客户端；如果URL指向CGI脚本，服务器就将脚本的运行结果传送到客户端。

首先要实现HTTP服务器。服务器的改动很简单。

```python
# cgisvr.py 文件
from http.server import HTTPServer, CGIHTTPRequestHandler # Python3
# Python2
# from BaseHTTPServer import HTTPServer
# from CGIHTTPServer import CGIHTTPRequestHandler
server = HTTPServer(('', 8000), CGIHTTPRequestHandler)
server.serve_forever()
```

对于POST方法的请求，它的URL需要指向一个CGI脚本(也就是在cgi-bin或者ht-bin中的文件)。CGIHTTPRequestHandler默认当前目录下的cgi-bin和ht-bin文件夹中的文件为CGI脚本，而存放于其他地方的文件被认为是静态文件。因此，需要修改index.html，将其中form元素指向的action改为cgi-bin/post.py。

```HTML
<html>
<head>
    <title>WOW</title>
</head>
<body>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
<form name="input" action="cgi-bin/post.py" method="post">
    First name:<input type="text" name="firstname"><br>
    <input type="submit" value="Submit">
</form>
</body>
</html>
```

创建文件夹和文件./cgi-bin/post.py，作为CGI脚本。在Linux需要执行权限。

```python
#!/usr/bin/env python
import cgi
form = cgi.FieldStorage() # 提取请求中包含的表格信息
# 输出到标准流，CGIHTTPRequestHandler会收集然后封装成HTTP响应报文。 
print "Content-Type: text/html"     # 报头，指定报文的内容
print                               # blank line, end of headers
print "<p>Hello world!</p>"         # Start of content
print "<p>" +  repr(form['firstname']) + "</p>"
```

CGI脚本可以执行更复杂的操作：数据库交互、页面交互等等。
