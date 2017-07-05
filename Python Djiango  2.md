

## Django

主要内容有：项目结构、urls路由语法、settings配置、ORM映射及数据库操作、HTML及模板渲染。

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
  ```
  如果pip升级经常失败，就https://pypi.python.org/pypi/pip/下载pip-*.tar.gz然后，解压，进入所在的磁盘和目录，

  ```bash
  python setup.py build
  python setup.py install
  ```

- 安装Django

  ```bash
  >pip install Django # linux必须sudo pip install Django
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
      │ templates  # html文件的归置目录，可选，自己新建
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

- 数据库初始化

  启动MySQL （5.5）

  ​	Windows/Linux，找到并且运行mysqld，然后终端`mysql -u root -p`，输入数据库密码

  创立数据库villa 

  ​	`mysql> CREATE DATABASE villa DEFAULT CHARSET=utf8;`

  创建用户django，并且将数据库Villa的所有权限都授予他

  ​	`GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON villa.* TO 'django'@'localhost' IDENTIFIED BY 'django';`

- 在django中设置数据库，修改sitedemo/sitedemo/settings.py

  ```python
  DATABASES = {'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'villa',  # 数据库名
      'USER': 'django',  # 用户名
      'PASSWORD': 'django',  # 密码
      'HOST': 'localhost',  # 数据库 ip
      'PORT': '3306',  # 数据库端口
  }}
  ```

- Django自带ORM，将数据库对象映射为Python对象。table---class，record/行---object，rank/列---实例属性。

  - Python2需要安装MySQL-python   `pip install mysql`

  - 而python3安装mysqlclient     `pip install mysqlclient`

    或者安装 pymysql  `pip install pymysql`，然后修改sitedemo/sitedemo/init.py

    ```python
    import pymysql  # 安装 pymysql 必须这样
    pymysql.install_as_MySQLdb()
    ```

  - 创建Model，在 sitedemo/west/models.py 增加一个类，就会在数据库增加一个table，类多一个属性，table就多一个column

    ```python
    from django.db import models
    class Character(models.Model):  # 角色
        name = models.CharField(max_length=200)  # 表只有一列，为name
        def __str__(self):  # Python2 是 __unicode__
            return self.name
    ```

  - 然后通知django，app中的models文件已被修改。终端运行： `python manage.py makemigrations west`

  - 再将models文件进行的修改映射到数据库中。终端运行：    `python manage.py migrate`

  - 数据库去看看操作是否成功。终端运行：

    ```mysql
    $mysql -u django -p # 输入用户django的密码登录数据库
    USE villa;
    SHOW TABLES;
    SHOW COLUMNS FROM west_character;
    ```

- 在网页显示数据库的内容

  - 往数据库填充数据。打开数据库，

    ```mysql
    INSERT INTO west_character (name) Values ('Jhon');
    INSERT INTO west_character (name) Values ('Django');
    INSERT INTO west_character (name) Values ('Lennon');
    SELECT * FROM west_character; # 查看是否成功
    ```

  - 修改app的view层，sitedemo/west/views.py 增加代码

    ```python
    from .models import Character  # 导入同级目录下的一个模块里面的一个类
    def showdata(request):
        staff_list = Character.objects.all()
        staff_str = map(str, staff_list)
        return HttpResponse('<p>%s</p>' % ' '.join(staff_str))
    ```

  - 修改路由文件，sitedemo/west/urls.py 增加代码

    ```python
    url(r'^showdata/', showdata),
    ```
    浏览器打开http://localhost:8000/west/showdata/




### **4. 使用html模板**

- 用简单的html模板进行渲染

  - 指定模板路径，编辑 sitedemo/sitedemo/settings.py

    ```python
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES = [
        {'DIRS': (
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'templates', 'west'), # 增加相关的内容
        ),
    ```

  - 编写html模板，新建并且编辑 sitedemo/templates/west/temp.html

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8", lang="en">
        <title>west template</title>
    </head>
    <body>
    <p>{{ label }}</p>  <!--依靠模板变量 label 传递数据-->
    </body>
    </html>
    ```

  - 编写相关的渲染函数， sitedemo/west/views.py 增加代码

    ```python
    from django.shortcuts import render
    def templay(request):
        staff_str_list = map(str, Character.objects.all())  # 取出数据表内所有的行，并且转化为字符串list
        staffs_str = ' '.join(staff_str_list)  # 字符串拼接
        context = {'label': staffs_str}  #指定渲染的内容。变量label与之对应
        return render(request, 'temp.html', context)  # 渲染到html中
    ```

  - 修改路由文件，sitedemo/west/urls.py 增加代码

    ```python
    urlpatterns = [
        url(r'^templay/', templay),  # 新增网页对应的一行
    ```

    浏览器打开http://localhost:8000/west/templay/

- html模板的循环、选择

  - 将 views.py 改为

    ```python
    def templay(request):
        staff_list = Character.objects.all()  # 取出数据表内所有的行
        return render(request, 'temp.html', {'staffs': staff_list})  # 渲染
    ```

  - 将 html 模板的`<body>`改为

    ```html
    {% for item in staffs %}
    <p>{{ item.id}}, {{item}}</p>  <!--item.id对象取值语法-->
    {% endfor %}
    ```

    Python的obj.attr对象属性的取值语法，可以直接用在html模板中。

    Python的for循环、if语法，都可以用在html模板中。

    选择结构也与Python类似。根据传送来的数据是否为True，Django选择是否显示。使用方式如下：

    ```html
    {% if condition1 %}
    <p>{{ item.id}}, {{item}}</p>  <!--display 1 -->
    {% elif condiiton2 %}
       ... display 2
    {% else %}
       ... display 3
    {% endif %}
    ```

- 模板的继承

  让templay.html 继承base.html。

  - 新建templates/west/base.html:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        {% block title %}
            <title>Title</title>
        {% endblock %}
    </head>
    <body>
        {% block body %}
            <p>origin paragraph</p>
        {% endblock %}
    </body>
    </html>
    ```

  - 在 temp.html中继承base.html，并替换特定block：

    ```html
    {% extends "base.html" %} <!--说明templay.html继承自base.html-->
    {% block title %} <!--用这个block替换base.html相应的block-->
        <title>loop</title>
    {% endblock %}
    {% block body %}
        {% for item in staffs %} <!--用for循环替换它-->
            <p>{{ item.id}}, {{item}}</p>
        {% endfor %}
    {% endblock %}
    ```




### **5. html与数据库联动**

- 表格——向网站递交数据

  HTML表格可以帮助用户构成HTTP请求，把数据用GET或者POST的方法，传递给某一URL地址。

  HTML文件，templates/west/getform.html

  ```html
  {% extends "base.html" %} <!--使用了模板文件-->
  {% block title %}
      <title>GET Form</title>
  {% endblock %}
  {% block body %}
      <form action="/west/get_data/" method="get"> <!--URL地址，请求方法-->
          <input type="text" name="staff"> <!--输入框，name值作为服务器的解析索引-->
          <input type="submit" value="Submit"> <!--提交按钮-->
      </form>
  {% endblock %}
  ```

  渲染函数， sitedemo/west/views.py 增加代码

  ```python
  def get_form(request):  # 发送最原始的网页
      return render(request, 'getform.html')
  def get_data(request):  # 处理数据
      data = request.GET['staff']
      return HttpResponse(data)
  ```

  路由文件，sitedemo/west/urls.py 增加代码

  ```python
  from .views import *
  urlpatterns = [
      url(r'^get_form/', get_form),  # 新增
      url(r'^get_data/', get_data),  # 新增
  ```

  浏览器打开http://localhost:8000/west/get_form/  输入内容，点击提交

  但是，用GET方法，有几个坏处：

  1. 不安全。是以`http://localhost:8000/west/get_data/?staff=Jhon`的方式，在URL中递交数据，
  2. 处理麻烦。发送表格和处理数据分为两步，views.py 和 urls.py 都分了两步

  改用POST方法，数据放在post中，并且一步处理。

  HTML文件，templates/west/postform.html

  ```html
  {% extends "base.html" %}
  {% block title %}
      <title>POST Form</title>
  {% endblock %}
  {% block body %}
      <form action="/west/post_form/" method="post"> <!--递交到同一个网址-->
          {% csrf_token %}  <!--防止跨站攻击-->
          <input type="text" name="staff"> <!--name值作为解析的索引-->
          <input type="submit" value="Submit">
      </form>
      <p>{{ post_str }}</p> <!--获得数据后，就显示在这里-->
  {% endblock %}
  ```

  渲染函数， sitedemo/west/views.py 增加代码

  ```python
  # 旧版的方式
  # from django.core.context_processors import csrf
  # def post_form(request):
  #     ctx ={}
  #     ctx.update(csrf(request))
  #     if request.POST:
  #         ctx['post_str'] = request.POST['staff']
  #     return render(request, "postform.html", ctx)
  from django.views.decorators.csrf import csrf_protect
  @csrf_protect
  def post_form(request):
      ctx ={}
      if request.method == 'POST':  # 最好不要用if request.POST:
          ctx['post_str'] = request.POST['staff']
      return render(request, "postform.html", ctx)
  ```

  路由文件，sitedemo/west/urls.py 增加代码

  ```python
  from .views import *
  urlpatterns = [
      url(r'^post_form/', post_form),  # 新增
  ```

  浏览器打开http://localhost:8000/west/post_form/  输入内容，点击提交

  ​

- 表格与数据库联合

  HTML文件修改，templates/west/postform.html

  ```html
  {% extends "base.html" %}
  {% block title %}
      <title>GET Form</title>
  {% endblock %}
  {% block body %}
      <form action="/west/post_form/" method="post">
          {% csrf_token %}
          <input type="text" name="staff">
          <input type="submit" value="Submit">
      </form>
      {% for person in staff %}
      <p>{{ person }}</p>
      {% endfor %}
  {% endblock %}
  ```

  渲染函数修改， sitedemo/west/views.py

  ```python
  from django.views.decorators.csrf import csrf_protect
  @csrf_protect
  def post_form(request):
      if request.method == 'POST':
          submitted = request.POST['staff']
          new_record = Character(name=submitted)
          new_record.save()
      ctx = {'staff': Character.objects.all()}
      return render(request, "postform.html", ctx)
  ```

- 使用表格对象

  一般，服务器会对client 提交的数据进行一些处理。比如数据校验（类型、长度）、数据类型转换。使用数据对象，就可以规定表格数据的类型和其它的一些要求，还可以获得数据后自动进行处理。

  渲染函数修改， sitedemo/west/views.py

  ```python
  from django import forms
  class CharacterForm(forms.Form):
      name = forms.CharField(max_length=200)  # 定义输入栏name的类型为字符串，最大长度为200
  from django.views.decorators.csrf import csrf_protect
  @csrf_protect
  def post_form(request):
      if request.method == 'POST':
          form = CharacterForm(request.POST)  # 根据POST，创立form对象
          if form.is_valid():  # 判断输入是否有效，并对输入进行预处理
              submitted = form.cleaned_data['name'] # 改变提取方式
              new_record = Character(name=submitted)
              new_record.save()
      form = CharacterForm()  # 再次创建一个空的form对象，并将它交给模板显示
      ctx = {'staff': Character.objects.all(),
             'form': form}
      return render(request, "postform.html", ctx)
  ```

  HTML文件修改，templates/west/postform.html

  ```html
  {% extends "base.html" %}
  {% block title %}
      <title>GET Form</title>
  {% endblock %}
  {% block body %}
      <form action="/west/post_form/" method="post">
          {% csrf_token %}
          {{ form.as_p }} <!--代替<input type="text" name="staff">用.as_p作为p标签-->
          <input type="submit" value="Submit">
      </form>
      {% for person in staff %}
      <p>{{ person }}</p>
      {% endfor %}
  {% endblock %}
  ```





### **6. 后台管理界面**

- 默认设置

  创建项目时，sitedemo/sitedemo/urls.py 默认带有管理界面地址

  ```python
  urlpatterns = [
      url(r'^admin/', admin.site.urls), # 后台 {site}/admin
  ```

  为了让admin界面管理某个数据模型，需要先注册该数据模型到admin。比如，west中的模型Character，修改west/admin.py:

  ```python
  from django.contrib import admin
  from .models import *  # 导入所有的Model
  admin.site.register(Character) # 用列表注册多个Model
  ```

  在终端创建管理员

  ```shell
  >python manage.py createsuperuser
  Username (leave blank to use 'user'): admin  # 用户名
  Email address: admin@admin.com  # 邮箱
  Password:  # 密码  github.com
  Password (again):
  Superuser created successfully.
  ```

  访问http://127.0.0.1:8000/admin，登录后，可以看到管理界面。

  这个页面除了west.characters外，还有用户和组信息。它们来自Django预装的Auth模块。我们将在以后处理用户管理的问题。

- 管理复杂的Model

  在 sitedemo/west/models.py 增加更复杂的数据表

  ```python
  class Customer(models.Model):
      name = models.CharField(max_length=200)
      age = models.IntegerField(default=0)
      email = models.EmailField()
      def __str__(self): return self.name
  class Tag(models.Model): # Tag以Contact为ForeignKey
      customer = models.ForeignKey(Customer)  # 一个Contact可以对应多个Tag
      name = models.CharField(max_length=50)
      def __str__(self): return self.name
  ```

  同步数据库更改：

  ​	`python manage.py makemigrations west`

  ​	`python manage.py migrate`

  修改west/admin.py:

  ```python
  admin.site.register([Character, Customer, Tag])  # 注册多个Model
  ```

- 自定义页面

  限制Model的可管理范围，修改west/admin.py:

  ```python
  class CustomerAdmin(admin.ModelAdmin):
      fields = ('name', 'age')  # 只可管理 name 和 age
  admin.site.register( Customer, CustomerAdmin) # 自定义后，这样注册
  admin.site.register([Character, Tag]) # 默认的，list注册
  ```

  还有很多自定义页面的技术，暂略，http://www.cnblogs.com/vamei/p/3548762.html




### **7. 用户管理 Session&Cookies**

虽然，在后台的管理界面，也能进行用户、用户组增删、权限设置，但是要正经地实现用户和会话管理，还是需要别的界面。

- 创建新的app  users

  终端，进入sitedemo目录运行`python manage.py startapp west`

  修改sitedemo/sitedemo/settings.py，增加这个app 及 模板目录

  ```python
  INSTALLED_APPS = [
      'users',  # 新增注册的app
  TEMPLATES = [
      {
          'DIRS': (
              os.path.join(BASE_DIR, 'templates', 'users'), # 新建的模板目录
  ```

- 登录并且跳转

  HTML文件修改，templates/users/signin.html

  ```html
  {% extends "base.html" %}
  {% block title %}
      <title>sign in</title>
  {% endblock %}
  {% block body %}
      <form action="auth/login/" method="post">
          {% csrf_token %}
          <label>UserName</label>
          <input type="text" name="username">
          <label>Password</label>
          <input type="text" name="pwd">
          <input type="submit" value="Submit">
      </form>
  {% endblock %}
  ```

  View层，templates/users/views.py

  ```python
  from django.shortcuts import render, redirect
  from django.contrib import auth
  from django.views.decorators.csrf import csrf_protect
  @csrf_protect
  def user_login(request):
      if request.method == 'POST':
          username = request.POST.get('username') # 如果没有输入，就得到空字符串
          password = request.POST.get('pwd')
          user = auth.authenticate(username=username, password=password)# 用户名密码检验
          if user is not None:
              if user.is_active:
                  auth.login(request, user)# 用户登入
                  return redirect('/hello/') # 重定向到一个登录成功页面。
              else: pass  # 返回一个“帐户已禁用”错误信息。
          else:pass  # 返回一个“无效用户名或密码”错误信息。
      return render(request, "signin.html")
  ```

  同时，增加路由。

  ```python
  # sitedemo/sitedemo/urls.py 
  import west.urls,users.urls
  urlpatterns = [
  	url(r'^auth/', include(users.urls)), # 新增
  # sitedemo/users/urls.py
  from django.conf.urls import url, include
  from .views import *
  urlpatterns = [url(r'^login/', user_login),]
  ```

  在管理界面增加一个用户和密码，浏览器打开http://localhost:8000/auth/login/，就可实现登录。

- 登出并且跳转

  View层，sitedemo//users/views.py

  ```python
  def logout(request):
      auth.logout(request)
      return redirect('/auth/login/') # 跳转到登录界面
  ```

  路由，sitedemo/users/urls.py

  ```python
  urlpatterns = [
      url(r'^logout/', logout),
  ```

  浏览器 访问 http://localhost:8000/auth/logout/就能登出

- 会话管理

  如何登录登出，只是用户会话管理的一小部分。这是对不同的用户提供不同服务的基础。

  对用户身份的检验，主要在views.py中进行。views.py是连接模型和视图的中间层，处理函数会处理 HTTP Request 并发回 Response 。在准备HTTP回复的过程中，就可以检验用户是否登陆，并且根据登陆与否，给出不同的回复。原理：

  ```python
  def diff_response(request):
      if request.user.is_authenticated():
          pass # 登录用户的网页
      else:
          pass # 未登录用户的网页
  ```

  request.user 是 contrib.auth.user 的一个实例对象。除了 is_authenticated() ，还有 get_username() 获取用户名、get_fullname() 获取全名、set_password() 设置密码、date_joined 账户创建时间、last_login 上次登录时间。

  但这样做比较麻烦，实际上用的一般都是装饰器。sitedemo//users/views.py

  ```python
  # 仅处理登录用户的请求，未登录就重定向到其他页面
  from django.contrib.auth.decorators import login_required
  @login_required()  
  def user_only(request):
      return HttpResponse("<p>message for logged in only.</p>")

  # 还可以写更复杂的校验，甄别用户，然后提供不同的服务
  from django.contrib.auth.decorators import user_passes_test
  def name_check(user):  # 定制筛选器
      return user.get_username().isalpha() # 用户名全是字母
  @user_passes_test(name_check) # 筛选器
  def special_user(request):
      return HttpResponse("<p>message for special user only.</p>")
  ```

  另外，还可以在模板中检验登录与否，然后给出不同的response：

  ```html
  {% if user.is_authenticated %}  <!--直接引用user实例-->
    <p>Welcome, user</p>
  {% else %}
    <p>Sorry, please login. </p>
  {% endif %}
  ```

- 用户注册

  用户注册的基本原理：建立一个提交用户信息的表格收集信息，相应的处理函数提取到这些信息后，建立User对象，并存入到数据库中。

  利用Django中的UserCreationForm生成表格，并在sitedemo//users/views.py中处理表格：

  ```python
  from django.contrib.auth.forms import UserCreationForm
  @csrf_protect
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              new_user = form.save()
              return redirect('/auth/login/') # 注册成功的跳转
          else:
              return HttpResponse("<p>sign up failed.</p>") # 注册失败报错
      else: # 第一次请求，返回 注册表格
          form = UserCreationForm()
          ctx = {'form': form}
          return render(request, 'signup.html', ctx)
  ```

  相应的HTML 

  ```html
  {% extends "base.html" %}
  {% block title %}
      <title>sign up</title>
  {% endblock %}
  {% block body %}
      <form action="/auth/signup/" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="Register btn">
      </form>
  {% endblock %}
  ```

  路由，sitedemo/users/urls.py

  ```python
  urlpatterns = [
      url(r'^signup/', signup),
  ```

