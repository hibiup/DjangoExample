## 新建 Django 项目：

~~~
django startproject DjangoExample
~~~

会生成如下目录：

~~~
DjangoExample\
  |-DjangoExample\
  |   |-settings.py
  |   |-urls.py
  |   |-wsgi.py
  |   |-__init__.py
  |-manage.py
~~~

其中根目录下的 manage.py 是 Django 的管理文件。DjangoExample/settings.py 是项目的配置文件。

## 添加 setup.py

在项目根目录下添加常规的 setup.py 文件(略)。

Django 有自己的一套 test case framework，为了让 setuptools 支持，需要在 setup.py 的 
setup() 中添加配置：

~~~
test_suite='tests.django_tests.run_tests'
~~~

也就是说我们需要在常规的 tests 目录下新建一个 django_tests.py 文件。并在其中定义一个 run_tests()
函数。详见 tests/django_test.py
