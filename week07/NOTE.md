# 本周作业
## 1.背景
实现《我是动物饲养员》这个游戏的部分开发任务。

## 2.具体要求
1. 定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化；
2. 动物园类要求有“名字”的属性和“添加动物”的方法，“添加动物”方法要实现同一种动物（同一个动物实例）不能被重复添加。
3. 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的标准是：“体型>=中等”并且是“食肉类型”同时“性格凶猛”；
4. 猫类要求定义“叫声”、“是否合适作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类；
## 3.测试
```
if __name__ == "__main__":
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化猫cat1
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    # 增加cat1到动物园
    z.add_amimal(cat1)
    # 判断动物园是否有cat1这只猫
    hava_cat = getattr(z, 'Cat')
```

# 一、一切皆对象（类）
1. self参数表示类的实例，指向当前实例的内存地址；
```
class Test(object):
    pass

# 实例化两个类a，b
a = Test()
b = Test()
# 查看实例化对象的类型
type(a)
# 查看实例化的内存地址
id(a)
# 查看实例化对象所属的类
a.__class__()
b.__class__()
# 类可以赋值
c = Test
d = c()
d.__class__()
```

# 二、类属性和实例属性
## 1.区别
1. 类属性在内存中只保存一份，对象属性在每个实例化之后都保存一份；
```
class Human(object):
    # 静态字段，类属性
    live = True
    def __init__(self, name):
        # 普通字段，对象属性
        self.name = name

# 实例化两个对象
man = Human('Adam')
woman = Human('Eve')

# 查看实例化对象的属性
man.__dict__

# 调用实例化属性。如果有，直接返回；没有则添加
man.name
man.live = False

man.live
woman.live
```
# 三、类属性的作用域
1. 单下划线+属性\
`_name`：人为不可修改
2. 双下划线+属性\
`__name`：私有变量，系统会给name改名达到私有化目的

# -四、类的方法：普通方法、类方法和静态方法
## 1.普通方法
至少有一个self参数，表示该方法的实例化对象.
### bound method 和 unbound method
类方法是unbound方法，实例化之后就是bound方法。差别是bound方法多了实例化过程。所以，方法的查找顺序是先从实例化的__dict__是否有该方法,如果没有，查找类方法。

## 2.类方法
### 类方法的引入
```
class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me = Kls2('wilson','yin')
me.print_name()

# 输入改为  wilson-yin
# 解决方法1: 修改 __init__()
# 解决方法2: 增加 __new__() 构造函数
# 解决方法3: 增加 提前处理的函数
def pre_name(obj,name):
    fname, lname = name.split('-')
    return obj(fname, lname)

me2 = pre_name(Kls2, 'wilson-yin')
me2.print_name()
```

### 语法
至少一个cls参数，表示该方法的类。要添加语法糖@classmethod.
```
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name

    # 类方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake

s = Story('anyone')
# 类和实例都可以使用
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())
```
类方法可以被类直接调用，也可以被实例化调用。

### 应用
[Python 中的 classmethod 和 staticmethod 有什么具体用途？
](https://www.zhihu.com/question/20021164)
1. 构造前交互
2. 特殊的构造函数
3. __new__等
4. 为以上函数提供子类hook点

## 3.静态方法
### 应用
不要和类的属性和方法产生联系的时候。
### 语法
由类调用，无参数。要添加语法糖@staticmethod

## 4.总结
有语法糖的方法（静态&类方法）都可以直接被类调用，而普通方法只能被实例化对象调用。


# 五、属性的处理__getattribute__() & __getattr__()
## 区别和联系
1. 联系：都可以对实例属性进行获取&拦截
2. 差异：前者对所有属性的访问都调用该方法，后者设适用于未定义的属性
## __getattribute__
```
class Human2(object):  
    """
    getattribute对任意读取的属性进行截获
    """  
    def __init__(self):
        self.age = 18
    # 固定写法
    def __getattribute__(self,item):
        print(f' __getattribute__ called item:{item}')

h1 = Human2()
h1.age      # 属性存在
h1.noattr   # 属性不存在
```
getattribute对任意读取的属性进行截获，所有属性均会调用__getattribute__方法
```
class Human2(object):  
    """
    拦截已存在的属性
    """  
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        print(f' __getattribute__ called item:{item}')
        # 用父类方法实现属性拦截。若存在，则返回；若不存在，则抛出异常
        return super().__getattribute__(item)
h1 = Human2()

# 存在的属性返回取值
print(h1.age)
# 不存在的属性返回 AttributeError
print(h1.noattr)
```
用父类方法实现属性拦截。若存在，则返回；若不存在，则抛出异常.
```
class Human2(object):    
    def __getattribute__(self, item):
        """
        将不存在的属性设置为100并返回,模拟getattr行为
        """
        print('Human2:__getattribute__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            # __dict__是存储属性的字典，如果没有该属性，则添加到dict
            self.__dict__[item] = 100
            return 100
h1 = Human2()
print(h1.noattr)
```
可以模拟__getattr__实现返回特定值。
## __getattr__
```
class Human2(object):  
    """
    属性不在实例的__dict__中,__getattr__被调用
    """
    def __init__(self):
        self.age = 18

    def (self, item): 
        print(f' __getattr__ called item:{item}')
        # 不存在的属性返回默认值 'OK'
        return 'OK'

h1 = Human2()

print(h1.age)
print(h1.hobby)
```
处理所有属性的返回值
```
class Human2(object):  
    def __init__(self):
        self.age = 18

    def __getattr__(self, item): 
        # 对指定属性做处理:fly属性返回'superman',其他属性返回None
        self.item = item
        if self.item == 'fly':
            return 'superman'
h1 = Human2()

print(h1.age)
print(h1.fly)
print(h1.noattr)
```
处理指定属性的返回值

## 两者的调用顺序
```
class Human2(object):    
    """
    同时存在的调用顺序
    """
    def __init__(self):
        self.age = 18
    def __getattr__(self, item): 
        print('Human2:__getattr__')
        return 'Err 404 ,你请求的参数不存在'
    def __getattribute__(self, item):
        print('Human2:__getattribute__')
        return super().__getattribute__(item)
h1 = Human2()

# 存在的属性用getattribute处理
print(h1.age)
# 如果属性不存在。如果同时两个函数存在
# 执行顺序是 __getattribute__ > __getattr__ > __dict__
print(h1.noattr)
```
属性若存在，用getattribute处理；
如果属性不存在。如果同时两个函数存在。执行顺序是__getattribute__ > __getattr__。如果还找不到，就去 __dict__字典中查找。

# 六、描述器原理 & 属性描述符
## 描述器Property
实现特定协议（描述符）的类，也就是说，property必须要基于一个类实现。描述器Property需要实现__get__()、__set__()、__delete__()方法。
1. get：得到类，也就是实例化类时，执行的方法；
2. set：修改类，也就是修改实例化类，执行的方法；
3. delete：删除类，也就是删除实例化类，执行的方法
```
# __getattribute__ 的底层原理是描述器
class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """
    def __init__(self, name):
        self.name = name
    # 实例化时，调用函数。第二个参数：实例化对象地址；第三个参数：实例化的类
    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__delete__{instance}')
        del self.name

class MyObj(object):
    # 实例化两个Desc对象
    a = Desc('aaa')
    b = Desc('bbb')

# 实例化MyObj对象
my_object = MyObj()
print(my_object.a)
# 修改对象属性
my_object.a = 456
print(my_object.a)
```

## 描述器Property优点
1 代码更简洁，可读性、可维护性更强。
2 更好的管理属性的访问。
3 控制属性访问权限，提高数据安全性。

## 描述器的高层实现
```
class Human2(object):
    def __init__(self):
        self._gender = None
    # 将方法封装成属性
    @property
    def gender2(self):
        print(self._gender)
    # 支持修改，固定写法，当执行修改操作，就调用该方法
    @gender2.setter
    def gender2(self,value):
        self._gender = value
    # 支持删除，固定写法，当执行删除操作，就调用该方法
    @gender2.deleter
    def gender2(self):
        del self._gender
h = Human2()
# 返回None
h.gender2
# 修改
h.gender2 = 'F'
# 返回‘F’
h.gender2
# 删除
del h.gender2
```
另一种property写法:
```
gender  = property(get_, set_, del_, 'other property')

```
## 纯Python实现property
```
class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
            self.__doc__ = doc
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)
```
## property样例之一
```
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100
```
## property样例之二
```
class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated_at = db.Column(db.DateTime) # 节点最后心跳时间
    state = db.Column(db.Integer, nullable=False) # 节点是否禁用

    @property
    def is_active(self):
        if(datetime.datetime.now() - self.updated_at).secondes > 60 \
            and self.vm_state == 0:
            return False
        return True
```
## property样例之三
```
from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from manage import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)

# 使用装饰器完成password的读取和写入功能分离
    @property
    def password(self):
        return None
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
  
    def is_active(self):
        return True
```

# 七、面向对象编程
## 新式类和经典类的区别
当前类/父类继承了object类，那么它是新式类。否则是经典类。
## object和type的关系
```
#__class__查看谁创建了自己，__bases__查看自己的父类
print('object：', object.__class__, object.__bases__)
print('type：', type.__class__, type.__bases__)
>>> object： <class 'type'> ()
>>> type： <class 'type'> (<class 'object'>,)
```
1. object和type都属于type类；
2. type类由type元类自身创建。object类是由元类type创建；
3. object的父类是空，没有继承自任何类
4. type的父类为object类
## 类的继承
广度优先，另外Python3中不加(object)也是新式类，但是为了代码不会误运行在python2下产生意外结果，仍然建议增加
1. 单继承
2. 多继承
3. 菱形继承
4. 继承机制MRO和C3算法
class_name.mro()查看类的继承情况
可以采用有向无环图解决多重继承的顺序问题。

# 八、SOLID设计原则与设计模式
## SOLID设计原则
1. 单一责任原则
每个类完成一项任务。
大类拆小类
2. 开放封闭原则
对扩展开放，对修改关闭。
子类继承父类+重构
3. 里氏替换原则
4. 依赖倒置原则
高层模块不应该依赖低层模块
5. 接口分离原则

这个solid原则主要针对静态语言，python语言主要关心前三个。
## 1.单例模式
### 定义
程序在实例时，只实例化1个实例。
### 1__new__()和__init__()的区别
1. 前者是实例创建前调用，后者是实例创建完成后调用
2. 前者是静态方法，返回实例对象，后者是实例方法
3. 前者先调用，后者后调用
4. 前者的返回值传递给后者的第一个参数，由后者设置实例对象的相关参数
```
class Foo(object):
    def __new__(cls, name):
        print('__new__() was running.')
        return super().__new__(cls)
    
    def __init__(self, name):
        print('__init__() was running.')
        super().__init__()
        self.name = name

bar = Foo('test')
bar.name

#相当于在执行下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')
```
### 实现方式
1. 装饰器
```
# 装饰器实现单实例模式
def singleton(cls):
    # 字典存储实例对象
    instances = {}
    # 函数判断实例是否存在
    def is_exit_instance():
        # 查看类是否在字典里
        if cls not in instances:
            # 把类的实例化装在字典里，键值对（类：类的实例化）
            instances[cls] = cls()
        return instances[cls]
    return is_exit_instance

@singleton 
class MyClass:
    pass

m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))
```
2. __new__()
单线程：
```
class Singleton2(object):
	__isinstance = False  # 默认没有被实例化
	def __new__(cls, *args, **kwargs):
		if cls.__isinstance:  
			return cls.__isinstance  # 返回实例化对象
		cls.__isinstance = object.__new__(cls)  # 实例化

		return cls.__isinstance
```
将一个类的实例绑定到类变量_instance上,
如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
如果cls._instance不为None,直接返回cls._instance
---
多线程
```
import threading
class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs: ## double check locking
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()
```
利用经典的双检查锁机制，确保了在并发环境下Singleton的正确实现。
但这个方案并不完美，至少还有以下两个问题：
·如果Singleton的子类重载了__new__()方法，会覆盖或者干扰Singleton类中__new__()的执行，
虽然这种情况出现的概率极小，但不可忽视。
·如果子类有__init__()方法，那么每次实例化该Singleton的时候，
__init__()都会被调用到，这显然是不应该的，__init__()只应该在创建实例的时候被调用一次。
这两个问题当然可以解决，比如通过文档告知其他程序员，子类化Singleton的时候，请务必记得调用父类的__new__()方法；
而第二个问题也可以通过偷偷地替换掉__init__()方法来确保它只调用一次。
但是，为了实现一个单例，做大量的、水面之下的工作让人感觉相当不Pythonic。
这也引起了Python社区的反思，有人开始重新审视Python的语法元素，发现模块采用的其实是天然的单例的实现方式。
·所有的变量都会绑定到模块。
·模块只初始化一次。
3. import实现单实例
```
# World.py
import Sun
def run():
    while True:
        Sun.rise()
        Sun.set()

# main.py
import World
World.run()
```
import机制是线程安全的（保证了在并发状态下模块也只有一个实例）。
### 注意
单实例模式如果用在多线程里面，要加锁
## 2.工厂模式
## 定义
根据传入参数不同，创建不同的实例对象
1. 工厂角色：判断参数，产生相应实例对象；
2. 抽象产品角色：公共接口（公共属性和方法）
3. 产品角色：具体每个对象类
## 分类
### 1.简单工厂模式
```
# 抽象产品角色
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

# 产品角色
class Man(Human):
    def __init__(self, name):
        print(f'Hi,man {name}')

# 产品角色
class Woman(Human):
    def __init__(self, name):
        print(f'Hi,woman {name}')

# 工厂角色
class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Adam", "M")
```
### 2.动态工厂模式
```
# 返回在函数内动态创建的类
def factory2(func):
    class klass: pass
    #setattr需要三个参数:对象、key、value
    setattr(klass, func.__name__, func)
    setattr(klass, func.__name__, classmethod(func))
    return klass

def say_foo(self): 
    print('bar')

Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()
```
## 3.元类
### 定义
1. 元类是创建类的类，类的模版；
2. 元类是用来控制如何创建类的，正如类是创建对象的模版一样
3. 元类的实例是类，正如类的实例是对象
### 创建方法
```
# 使用type元类创建类
def hi():
    print('Hi metaclass')

# type的三个参数:类名、父类的元组、类的成员
Foo = type('Foo',(),{'say_hi':hi})
foo = Foo
foo.say_hi()
# 元类type首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力

```

```
def pop_value(self,dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break

# 元类要求,必须继承自type    
class DelValue(type):
    # 元类要求，必须实现new方法
    def __new__(cls,name,bases,attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls,name,bases,attrs)
 
class DelDictValue(dict,metaclass=DelValue):
    # python2的用法，在python3不支持
    # __metaclass__ = DelValue
    pass

d = DelDictValue()
d['a']='A'
d['b']='B'
d['c']='C'
d.pop_value('C')
for k,v in d.items():
    print(k,v)
```
## 4.mixin模式
### 定义
在程序运行过程中，重定义类的继承，即动态继承。
优点：
1. 可以在不修改任何源代码的情况下，对已有类进行扩展；
2. 可以进行组件的划分