# 解决mysqlclient安装不成功的办法
```
macOS (Homebrew)

Install MySQL and mysqlclient:

Assume you are activating Python 3 venv
$ brew install mysql

$ pip install mysqlclient

If you don't want to install MySQL server, you can use mysql-client instead:

Assume you are activating Python 3 venv
$ brew install mysql-client

$ echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile

$ export PATH="/usr/local/opt/mysql-client/bin:$PATH"

$ pip install mysqlclient
```
# 包和模块
假设有以下目录：\
package/subpackage/print.py\
package/\__init__.py\
package/hello.py\
package/name.py\
print.py
```
print("This is print.py")
```

\__init__.py
```
print("Hello Package!")
```

hello.py
```
def func_hello():
    print("This is hello.py")

if __name__ == "__main__":
    func_hello()
```

name.py
```
from . import hello

print("-"*30)
hello.func_hello()
print("This is name.py")
print("-"*30)
```
## 模块和包
一个.py文件被称作模块，多个.py文件放在一个文件夹中被称为包
## 如何理解`if __name__ == '__main__'`这句话？
如果模块是被直接运行的，则if里面的代码块被运行，如果模块是被导入的，则if中的代码块不被运行。
## 同一个包中模块的相互引用
1. 同级模块间引用\
1.import module_name\
导入之后就可以使用这个模块中的所有函数\
module_name.function_name()\
2.from module_name import function_name/function_0, function_1\
导入某个模块中特定的函数\
3.as可以给模块和函数取别名
2. 上级模块引用下级模块\
hello.py\
`from .subpackage import print`\
表示从subpackage包中导入print模块
3. 下级模块引用上级模块\
print.py\
`from .. import hello`\
表示导入hello模块

# 开发环境配置
Django = 2.2.13\
查看Django版本：`python -m django --version`

# Django简要介绍
Django是一组开发Web应用程序的框架，用Python编写完成。能够快速相应网页请求，轻松读写数据库和管理用户等。

# Django创建项目、App和启动
1. `django-admin startproject project_name . `
2. `python manage.py startapp app_name`
3. `python manage.py runserver IP:Prot`

# Django.settings主要配置
## INSTALLED_APPS添加APP
一个app完成一个web功能

## TEMPLATES模版相关
1. 修改模版引擎
2. 设置模版路径
3. 在app中查找模版文件

## DATABASES数据库设置
默认是sqlite3
修改成mysql
```
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'rootroot',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
```

## LANGUAGE_CODE和TIME_ZONE
`LANGUAGE_CODE = 'zh-hans'`

`TIME_ZONE = 'Asia/Shanghai'`

# Django的路由分发
1. 从project/urls.py中分发路由到每个App的urld.py中；
2. app/urls.py中的路由又分发到对应的views中；
3. 在app/views.py中，导入app/models.py中定义的模型，进行crud操作；
4. 然后返回templates中对应的HTML模版

# URLS匹配和接收变量
## 1.字符串匹配
```
app/urls.py
path('index/', views.index),

app/views.py
def index(resquest):
    return HttpResponse("Hello Django!")
```
## 2.带变量匹配
```
app/urls.py
path('<str:name>/<int:age>', views.student),

app/views.py
def student(resquest, **stuInfo):
    return HttpResponse("我的名字%s是，今年%s岁。"%(stuInfo['name'], stuInfo['age']))
```
变量用字典操作
## 3.正则匹配
```
app/urls.py
re_path('(?P<year>\d{4})', views.year, name='yearurl'),

app/views.py
def year(resquest, year):
    return HttpResponse("现在是%s年。"%(year))
```

## 4.自定义匹配（自定义正则和带变量）
```
app/urls.py
register_converter(converters.phoneNumConverter, 'test')
path('<test:phonenum>', views.phonenum),

app/views.py
def phonenum(resquest, phonenum):
    return HttpResponse("我的电话号码是：%s"%(phonenum))

app/converters.py
class phoneNumConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
```

# 视图的快捷函数
绑定模版文件和视图views。
## render函数
把请求request转移到html页面中
## redirect函数
重定向请求，本质是重新解析html页面
## get_object_or_404函数

# models.py 与数据库
## 处理好Django和数据库的连接，特别是版本和依赖包的问题
learn more refer to F&A
## ORM（Object/Relation Mapping，简称ORM）
定义一种元数据`type = models.CharField(max_length=20)
`，将面向对象语言中的对象转化到数据库中
## ORM操作的两条命令(ORM->数据库)
```
python manage.py makemigrations
python manage.py migrate
```
1. 将元数据转化为sql语言，生成sql语言文件
2. sql语言commit到数据库中，存储在数据库中
3. 执行这两条是需要迁移额外的管理django的数据表

## ORM_API：一定要注意字符集
> from index.models import *
### 增加
> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')

### 删除
单条数据
>Name.objects.filter(name='红楼梦').delete()

全部数据
>Name.objects.all().delete()
### 修改
> Name.objects.filter(name='红楼梦').update(name='石头记')

### 查询
>Name.objects.get(id=2).name
> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>Name.objects.create(name='活着', author='余华', stars='9.4')
>Name.objects.all()[0].name
>n = Name.objects.all()
> n[0].name
> n[1].name
>Name.objects.values_list('name')
>Name.objects.values_list('name')[0]
filter支持更多查询条件
filter(name=xxx, id=yyy)
## 数据库->ORM对象
```
python manage.py inspectdb > app_name/models.py
```
Mate类是一个元数据类，与数据表无关。
`managed = False`是为了防止数据出错设置的。


# 模版相关
## 模版变量
{{ variables }}
## 从URL获取模版变量
{% url 'urlyear' 2020 %}
把2020传递给URL.name = 'urlyear' 的url地址
## 读取静态资源内容
{% static 'css/header.css'%}
## for循环
{% for type in type_list %}
{% endfor %}
## if判断
{% if name.type == type.type %}
{% endif %}

# 将数据库中的内容展示到templates
app/viwes.py
```
def booklist(resquest):
    n = Info.objects.all()
    # locals函数将函数中所有的变量传递给templates
    return render(resquest, 'books.html', locals())
```
app/templates/books.html
```
{% for book in n%}
    <div>
        bookname:{{ book.name}}<br>
        author:{{ book.author}}<br>
        rate:{{book.rate}}<br>
    </div>
{% endfor %}
```
# F&A
1. 为什么一定要给正则命名？name参数的作用？
```
re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear')
```
name参数等价于匹配到的url，方便后续程序使用，用于解耦

2. 解决Django和mysql连接的问题
1 django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
解决方法：在 __init__.py 文件中添加以下代码即可
import pymysql
pymysql.install_as_MySQLdb()

2   version = Database.version_info
# if version < (1, 3, 13):
# raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

3  AttributeError: 'str' object has no attribute 'decode'
出现这个错误之后可以根据错误提示找到文件位置，打开 operations.py 文件，找到以下代码：
def last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    # if query is not None:
    #     query = query.decode(errors='replace')
    return query

注意：mysql客户端的环境变量（which mysql）





