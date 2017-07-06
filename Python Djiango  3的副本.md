

<<<<<<< HEAD
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





=======
## 开发环境配置

##### 安装MySQL

- Ubuntu > `sudo apt-get install mysql-server mysql-client libmysqlclient-dev `
- Windows 略

##### 安装Python，升级pip

- 安装Python：略

- 配置pip：一般来说，Python官网连接不稳定，创建C:\Users\${usrname}\pip\pip.ini，并且写入

  ```batch
  [global]
  trusted-host=pypi.v2ex.com
  index-url=index-url=http://pypi.v2ex.com/simple
  ```

- 升级pip

  ```batch
  python -m pip install -U pip  # 用pip自己升级
  ```

  如果pip升级经常失败，就https://pypi.python.org/pypi/pip/下载pip-*.tar.gz然后，解压，进入所在的磁盘和目录，

  ```bash
  python setup.py build
  python setup.py install
  ```


##### 创建虚拟环境

如果只有一个Python，所有第三方的包都会被安装到`site-packages`目录下。可能工程1要用jinja 2.7，而工程2要用jinja 2.6就会相互冲突。这时候就可以用 virtual environment 进行隔离。

- 安装virtualenv 

    `python2 -m pip install virtualenv`，

   python3有venv模块，所以不需要安装

- 进入创建虚拟环境的文件目录，然后建立虚拟环境“djvenv”

  Python2运行  `python -m virtualenv djvenv`

  Python3运行  `python -m venv djvenv`

- 激活虚拟环境：

  Win`>%cd%\djvenv\Scripts\activate.bat`

  Unix`>./djvenv/bin/activate`

- 在虚拟环境 djvenv 安装 MySQL数据库驱动

   `python -m pip install mysql`

   `python3 -m pip install mysqlclient`

- 在虚拟环境 djvenv 安装 Django

  ```bash
  >python -m pip install Django #linux要sudo。可以Python3
  >python
  >>> import django
  >>> django.get_version()
  '1.11.2'
  ```

- 注：检查现有环境已经安装的包 `pip list`，运行`activate`文件进入虚拟环境，输入 `deactivate`退出虚拟环境的命令

##### 安装配置 Apache 或 Ngnix





### 初始化Django项目

- 切换到指定的virtual env（也就指定了Python2还是Python3）

  然后在djlearn目录下运行`django-admin.py startproject mysite`

  因为运行这个工程，需要指定这个虚拟环境的Python启动manage.py。为了方便指定，编写bat和sh脚本。

  run.bat是Windows启动开关

  ```powershell
  @echo off
  set mysqlDIR="C:\Program Files (x86)\MySQL\MySQL Server 5.5\bin"
  cd mysqlDIR && net stop mysql & net start mysql
  set DIR=%~dp0
  set /p ip=please input server ip:(default 0.0.0.0):
  if "%ip%"=="" ( set ip=0.0.0.0)
  set /p port=please input server port:(default 9000):
  if "%port%"=="" ( set port=9000)
  echo "ip: %ip% port:%port%"
  "%DIR%\djvenv\Scripts\python.exe" "%DIR%\mysite\manage.py" "runserver" "%ip%:%port%" %*
  :finally
  pause
  echo.
  ```

  Unix的启动开关

  ```shell
  #!/bin/sh
  service mysql stop; service mysql start
  DIR==$(cd `dirname $0`; pwd)
  Python=${DIR}/djvenv/bin/python
  manage=${DIR}/mysite/manage.py
  echo "please input server ip:(default 0.0.0.0)"; read ip
  if [ "$ip" == "" ];then ip="0.0.0.0";fi
  echo "please input server port:(default 9000)"; read port
  if [ "$port" == "" ];then port="9000";fi
  echo "ip: $ip port: $port"
  exec  "${Python} ${manage} runserver ${ip}:${port}"
  ```

  最后整个工程如下：

  ```python
  djlearn # 本项目的总文件夹
  ├─run.bat # Windows启动开关
  ├─run.sh  # Unix 启动开关
  ├─templates   # 模板文件夹
  ├─static   # media/js/css等等
  ├─djvenv  # 本项目的Python virtual env
  └─mysite # 源代码总文件夹，相当于src
      │  manage.py # 管理器，相当于main
      └─mysite # 项目的主要源代码目录
              settings.py
              urls.py
              wsgi.py
              __init__.py
  ```

  在djlearn目录里，运行

  - `%cd%\djvenv\Scripts\activate.bat`     激活本项目的virtual env
  - 切换目录  `cd mysite`
  - `python %cd%\mysite\manage.py makemigrations`   
  - `python %cd%\mysite\manage.py migrate`    两步让项目的修改生效






### 创建第一个app

- 初始化 

  - 在djlearn文件夹，激活venv  `%cd%\djvenv\Scripts\activate.bat`，切换目录  `cd mysite`
  - 创建 "polls" app   `>python manage.py startapp polls`
  - 在djlearn/mysite/mysite/settings.py 内，在变量`INSTALLED_APPS = [`里，加上一行`'polls.apps.PollsConfig',`
  - 运行两句命令`python manage.py makemigrations;python manage.py migrate`让项目的修改生效

- 构建views。文件 djlearn/mysite/polls/views.py

  ```python
  from django.http import HttpResponse
  def index(request):
      return HttpResponse("polls index")
  ```

- 构建urls。url函数有4个参数：正则表达式，view函数，关键词参数，链接名

  - djlearn/mysite/mysite/urls.py 增加  `url(r'^polls/', include('polls.urls')),`

  - djlearn/mysite/polls/urls.py 增加 

    ```python
    from django.conf.urls import url
    from . import views  # 从本文件夹导入
    urlpatterns = [url(r'^$', views.index, name='index'),] 
    ```

- 运行两句命令`python manage.py makemigrations;python manage.py migrate`让项目的修改生效




### 使用数据库

MVC 和 MTV 的对比

| 模型   | 数据库      | 业务处理        | 界面展现        |
| :--- | -------- | ----------- | ----------- |
| MVC  | Model 模型 | Control 控制器 | View 视图     |
| MTV  | Model 模型 | View 渲染     | Template 模板 |

##### 数据库初始化C:\Program Files (x86)\MySQL\MySQL Server 5.5\bin\mysqld.exe

- 启动MySQL （5.5）：Windows/Linux，找到并且运行mysqld，然后终端`mysql -u root -p`，输入数据库密码
- 创立数据库dj ，设置字符： `mysql> CREATE DATABASE dj DEFAULT CHARSET=utf8;`
- 创建用户django，并且将数据库 dj 的所有权限都授予他：`GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON dj.* TO 'django'@'localhost' IDENTIFIED BY 'django';`


- 配置文件 djlearn/mysite/mysite/settings.py 

  ```python
  DATABASES = {'default': {
      'ENGINE': 'django.db.backends.mysql', # django相应的数据库组件
      'NAME': 'dj', # 数据库名。SQLite指定一个特定的文件路径
      'USER': 'django', # 用户名
      'PASSWORD': 'django', # 密码
      'HOST': '127.0.0.1', # 
      'PORT': '',
  }}
  ```



##### 创建Django数据模型

- djlearn/mysite/polls/models.py 

  ```python
  import django.db.models as models; import datetime
  from django.utils import encoding, timezone
  @encoding.python_2_unicode_compatible
  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')
      def __str__(self):return self.question_text
      def was_published_recently(self):
          return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  @encoding.python_2_unicode_compatible
  class Choice(models.Model):
      question = models.ForeignKey(Question, on_delete=models.CASCADE)
      choice_text = models.CharField(max_length=200)
      votes = models.IntegerField(default=0)
      def __str__(self):return self.choice_text
  ```

##### 提交

- 生成对应的SQL操作语句：`$  python manage.py makemigrations polls`
- 执行SQL操作：`$ python manage.py migrate`

##### 使用Django数据库接口

- CRUD例子如下

  ```python
  # Create增 q = Question(question_text="What's new?", pub_date=timezone.now())
  # Retrieve查询所有 Question.objects.all()
  # 查询过滤 Question.objects.filter(id=1)
  # 查询一个 q = Question.objects.get(pk=1)
  # Update改 q.question_text = "What's up?"
  # Delete删 c.delete()
  ```

##### 使用后台管理界面

- 创建 Admin 用户：`$ python manage.py createsuperuser`
- 启动 Django 项目，然后进入管理界面




### 构建views

- 最简单的views：截获url，返回response

  - urls：

    djlearn/mysite/mysite/urls.py 增加  `url(r'^polls/', include('polls.urls')),`

    djlearn/mysite/polls/urls.py 增加 `urlpatterns = [url(r'^$', views.index, name='index'),]`

  - views： djlearn/mysite/polls/views.py

    ```python
    def index(request):return HttpResponse("polls index")
    ```

- 让 urls 与 views 交互

  - urls：djlearn/mysite/polls/urls.py：

    ```python
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    ```

    ` ?P<question_id>`定义了正则名称，而`[0-9]+`是正则式。二者组建了类似于`question_id='34'`的函数参数。

    - 浏览器请求`http://site//polls/34/`
    - djlearn/mysite/mysite/urls.py 的  `url(r'^polls/', include('polls.urls')),`截获了`http://site//polls/`，然后将`34/`转交给djlearn/mysite/polls/urls.py
    - djlearn/mysite/polls/urls.py的`url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),`截获`34/`，用正则组装信息（也可能不组装），然后调用函数
    - 调用函数`detail(request=<HttpRequest object>, question_id='34')`

  - views： djlearn/mysite/polls/views.py

    ```python
    def detail(request, question_id): # question_id 参数由正则表达式而来
        return HttpResponse("You're looking at question %s." % question_id)
    ```

- 更复杂的views

  所有的view函数，要么发回一个HTTP Response（数据库、template渲染、读取文件…），要么引发异常（比如404）。

  改写/polls/views.py的 index() 函数，浏览器打开http://localhost:9000/polls/

  ```python
  def index(request): # 读取数据库然后渲染
      latest_question_list = Question.objects.order_by('-pub_date')[:5]
      output = ', '.join([q.question_text for q in latest_question_list])
      return HttpResponse(output)
  ```

- 1
>>>>>>> origin/master
