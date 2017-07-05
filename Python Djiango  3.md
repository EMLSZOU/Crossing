### 安装配置数据库

MySQL，略

启动MySQL （5.5）

​	Windows/Linux，找到并且运行mysqld，然后终端`mysql -u root -p`，输入数据库密码

创立数据库villa ，设置字符

​	`mysql> CREATE DATABASE villa DEFAULT CHARSET=utf8;`

创建用户django，并且将数据库Villa的所有权限都授予他

​	`GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON villa.* TO 'django'@'localhost' IDENTIFIED BY 'django';`

### 安装Python，升级pip

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




### 创建虚拟环境

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

- 安装MySQL数据库驱动

   `python -m pip install mysql`

   `python3 -m pip install mysqlclient`

- 安装 Django

  ```bash
  >python -m pip install Django #linux要sudo。可以Python3
  >python
  >>> import django
  >>> django.get_version()
  '1.11.2'
  ```

- 注：检查现有环境已经安装的包 `pip list`，运行`activate`文件进入虚拟环境，输入 `deactivate`退出虚拟环境的命令

### 安装配置 Apache 或 Ngnix



### 初始化Django项目

- 切换到指定的virtual env（也就指定了Python2还是）

  然后在djlearn目录下运行`django-admin.py startproject mysite`

  因为运行这个工程，需要指定这个虚拟环境的Python启动manage.py。为了方便指定，编写bat和sh脚本。

  run.bat是Windows启动开关

  ```powershell
  @echo off
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

- 构建urls

  - djlearn/mysite/mysite/urls.py 增加  `url(r'^polls/', include('polls.urls')),`

  - djlearn/mysite/polls/urls.py 增加 

    ```python
    from django.conf.urls import url
    from . import views  # 从本文件夹导入
    urlpatterns = [url(r'^$', views.index, name='index'),]
    ```

- 运行两句命令`python manage.py makemigrations;python manage.py migrate`让项目的修改生效

### 使用数据库

- 数据库初始化

  启动MySQL （5.5）

  ​	Windows/Linux，找到并且运行mysqld，然后终端`mysql -u root -p`，输入数据库密码

  创立数据库dj

  ​	`mysql> CREATE DATABASE dj DEFAULT CHARSET=utf8;`

  创建用户django，并且将数据库Villa的所有权限都授予他

  ​	`GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON dj.* TO 'django'@'localhost' IDENTIFIED BY 'django';`

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

  ​

- 1
