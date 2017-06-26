

## Django



### **1.安装：**

- 配置pip：一般来说，Python官网连接不是很好，创建C:\Users\${usrname}\pip\pip.ini，并且写入下文

  ```batch
  [global]
  trusted-host=pypi.v2ex.com
  index-url=index-url=http://pypi.v2ex.com/simple
  ```

- 升级pip

  ```batch
  python -m pip install -U pip  # 用pip自己升级
  # 如果升级失败，可以
  ```
  如果pip升级经常失败，就https://pypi.python.org/pypi/pip/下载pip-*.tar.gz然后，解压，进入所在的磁盘和目录，

  ```bash
  python setup.py build
  python setup.py install
  ```

- 安装Django

  ```bash
  >pip install Django :: linux必须sudo pip install Django
  >python
  >>> import django
  >>> django.get_version()
  '1.11.2'
  ```

**启动项目：**

- 生成初始文件，进入文件夹web，运行

  ```bash
  django-admin.py startproject sitedemo
  ```

  查看生成的文件树（Win用tree /f，Linux用tree）

  ```bash
  D:\web
  └─sitedemo       # 包裹文件夹，名字可以任意
      │ manage.py  # 管理主程序
      │ templates  # html文件的归置目录，可选
      └─sitedemo   # 真正的工程目录
            settings.py  # 主配置文件
            urls.py      # url 路由文件
            wsgi.py      # 网络通信接口
            __init__.py
  ```

- 进入manage.py所在的文件夹，运行

  ```bash
  python manage.py runserver 8000
  ```

  另一种在Pycharm中设置运行的方式

  ```bash
  Script选项：manage.py的完整路径，比如D:\web\sitedemo\manage.py
  Working Directory选项：manage.py所在的目录，比如D:\web\sitedemo
  Script parameters选项：runserver 127.0.0.1:8000
  右击manage.py，选run可以自动生成前两个选项，然后"菜单栏/Run/ EditConfigurations"手动填写Script parameters
  ```

- 浏览器打开 http://localhost:8000/

  ```bash
  It worked!
  Congratulations on your first Django-powered page.
  ```






### **2. Hello World!**

服务器是“请求-回应”的工作模式，客户向URL发送请求（点单），服务器根据请求，开动后厨，并最终为客人上菜。Django采用的MVC结构，即点单、厨房、储藏室分离。

- 返回字符串

  点单：接收请求，将URL对应分配给某个对象处理。修改sitedemo/sitedemo/urls.py

  ```python
  from django.conf.urls import url, include
  from django.contrib import admin
  from .views import hello  # 导入对应的views模块
  urlpatterns = [
      # url(r'^admin/', admin.site.urls), # 后台页面，先注释掉
      url(r'^hello/', hello),  # 新增映射。(正则表达式，业务逻辑函数)
  ]
  ```

  然后在sitedemo/sitedemo创建views.py

  ```python
  from django.http import HttpResponse  # 必须导入这个模块
  def hello(request):  # 必须有request参数（相当于self），代表用户请求报文
      return HttpResponse('<p>\n Hello World!</p>')  # 返回一个字符串构建的实例
  ```

  这2步，便将http://localhost:8000/hello/这个url指向了views里的hello()函数，它接收用户请求，并返回一个“Hello World”字符串。

  运行manage，浏览器打开http://localhost:8000/hello/，就能看到Hello World

- 返回HTML页面

  修改sitedemo/sitedemo/urls.py，新增一条映射

  ```python
  url(r'^hypertext/', hypertext),
  ```

  修改sitedemo/sitedemo/views.py，相应地新增一个函数

  ```python
  from django.shortcuts import render  # 必须导入这个模块
  def hypertext(request):
      return render(request, "hypertext.html")  # 用render渲染html文件
  ```

  修改sitedemo/sitedemo/settings.py，指定html文件的路径

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')], # 只改这一点
  ```

  新建文件sitedemo/templates，归置页面。相应地，在下面新建 hypertext.html 文件

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>satic</title>
  </head>
  <body>
      <h1 style="color:red">HTML page</h1>
  </body>
  </html>
  ```

- 返回静态页面（HTML/CSS/Js）




**增加 app**

进入sitedemo目录（不是sitedemo/sitedemo）运行

```bash
python manage.py startapp west
```

于是这个sitedemo文件夹下，多了一个west文件夹。

```bash
├─sitedemo
│  ├─ __init__.py
│  ├─ manage.py
│  ├─ sitedemo
│  ├─ templates
│  └─ west  # 新增的文件夹 
```

修改sitedemo/sitedemo/settings.py，增加这个app

```python
INSTALLED_APPS = [
    'west',  # 新增这一行
```

本来，在母程序的sitedemo/sitedemo/urls.py指定url映射就可，但一般为了解耦，会在sitedemo/sitedemo/urls.py指定 west/urls.py ，而在 west/urls.py详细指定具体的url

- 修改 sitedemo/sitedemo/urls.py

  ```python
  import west.urls
  url(r'^west/', include(west.urls)),
  ```

- 新增 sitedemo/west/urls.py

  ```python
  from .views import apphello
  urlpatterns = [
      url(r'^apphello/', apphello),
  ]
  ```

- 修改 sitedemo/west/views.py

  ```python
  from django.http import HttpResponse
  def apphello(request):
      return HttpResponse('<p>\n app Hello</p>')
  ```

启动Django，浏览器打开http://localhost:8000/west/apphello/，显示”app Hello“





### **3. 数据库**

- 初始化

  启动MySQL

  ​	Windows，找到并且运行mysqld.exe，然后在终端`mysql`

  ​	Linux，终端`mysql -u root -p`

  创立数据库

- ​

