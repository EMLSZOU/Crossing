

# 在 Linux 部署 Django

在控制台开启 Ubuntu 的 SSH 连接：

​	`sudo apt-get update;`

​	`sudo apt-get install openssh-server`

Mac SSH 远程连接Ubuntu   {username}代表变量，比如用户名 aching

​	`ssh {username}@10.211.55.7`或`ssh 10.211.55.7 -l {username}`

1. ### 安装MySQL

   终端执行 `>sudo apt-get install mysql-server mysql-client`

2. ### 安装 Apache 或者 Nginx，配置 WSGI

   在终端输入：

   `sudo apt-get install apache2;`

   `sudo apt-get install libapache2-mod-wsgi`

   配置 Apache，在文件 /etc/apache2/apache2.conf 末尾追加

   ```html
   # Django
   Alias /media/ /home/aching/media
   <Directory /home/aching/media>
   Order deny, allow
   Require all granted
   </Directory>
   Alias /static/ /home/aching/static
   <Directory /home/aching/static>
   Order deny, allow
   Require all granted
   </Directory>
   WSGIScriptsAlias /  /home/aching/mysite/wsgi.py
   WSGIPythonPath  /home/aching/mysite
   <Directory /home/aching/mysite/mysite>
   <Files wsgi.py>
       Order deny, allow
       Require all granted
   </Files>
   </Directory>
   ```

   media 和 static 文件夹的设立，是因为：Django的py文件主要是为了动态地生成HTTP Response。如果浏览器请求静态资源（media、js、css），服务器响应无非就是读取特定的文件并且组成报文发送，这让 WSGI 处理会比 Django 更快。

3. ### 准备Python环境

   安装 Python：`sudo apt-get install python`

   ​	python3: ` sudo apt-get install python3`

   升级pip：`sudo python -m pip install -U pip`

   ​	python3:  `sudo python -m pip install -U pip`

   建立虚拟环境：`sudo python -m pip install virtualenv`

   ​	Python3： `sudo python3 -m pip install virtualenv`

   安装 MySQL 的 Python 驱动

4. ### 安装 Django

   `sudo pip install django`

   ​

   `sudo pip3 install django`

5. ### 创建项目，并且启动项目





