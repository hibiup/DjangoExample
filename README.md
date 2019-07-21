Django 是一个基于 Python 的 Web 项目工具（对于微服务来说太重了），但是如果用于一个 Web 网
站，它模块化的设计让我们能很快开发出需要的内容。


## 新建 Django 项目：

```
$ django-admin startproject DjangoExample
```

`django-admin` 是 Django 的管理命令，它可以用来管理 Django 项目。以上命令会生成如下目录：

```
DjangoExample\
  |--DjangoExample\
  |  |--settings.py
  |  |--urls.py
  |  |--wsgi.py
  |  |--__init__.py
  |--manage.py
```

* manage.py    Django 的命令行项目管理工具。
* settings.py  项目的配置文件。
* wsgi.py      与 WSGI 兼容的 Web 服务器的入口，用于运行项目。
* urls.py      项目的 URL 配置文件

### 添加 setup.py

在项目根目录下添加常规的 setup.py 文件(略)。

### 开发与调试

#### 初始化

Django 会生成一个缺省页面和一个缺省管理台，可以在 `urls.py` 中看到 `admin/` 路径。但是此
时还不能登录，需要初始化网站：

```
$ python manager.py makemigrations   # 删除所有内容
$ python manage.py migrate           # 初始化数据库。Django 缺省使用 sqlite3 作为数据库。
```

可以在 settings.py 的 `DATABASE` 节下修改数据库配置（略）。

先创建一个管理员：

```
$ python manage.py createsuperuser
Username (leave blank to use 'xxxx'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

#### 启动项目

进入项目目录启动项目：

```
$ python manage.py runserver 0.0.0.0:8000
```

#### 退出

`Ctrl-C`

### 开发

#### 添加页面

缺省的 DjangoExample 是缺省的根目录。首页 `index.py` 面新建在这个目录下。然后修改 `urls.py`，
将它设置为缺省页面(正则匹配 `r'^$'` )。Django 支持热加载，无需重启即刻刷新页面看效果。

#### 添加应用模块(app)：

Django 中 `Project` 为顶级，`app` 代表模块:

```
$ python manage.py startapp app1
```

在项目根目录下新建了一个名为 `app1` 的应用目录。生成的文件大多为空，除了 apps.py。在 app1 
目录下添加模块缺省页面。（参见 `app1/viwes/index.py`），并注册 url (参见 `DjangoExample\urls.py`)

##### 单元测试

然后编写单元测试，模块缺省在模块根目录（app1/）下生成 tests.py 文件，可以新建到 `app1/tests`
子目录下，无需修改配置。单元测试编写参见 `app1/tests/tests.py`

注意，Django 用自己的 TestCase 基类，IDEA 缺省使用 unittest，因此直接用 IDEA 执行测试会
报出 `TypeError: argument of type 'ConnectionHandler' is not iterable` 错误。需要
在整个项目的根目录（不是 app1/ 目录）下利用 Django 的 manager.py 命令行执行单元测试，
manager.py 会自动找到测试文件：

```
$ python manage.py test     # 需要更多输出信息可选参数：-v 2
```

参考：http://www.runoob.com/django/django-first-app.html
