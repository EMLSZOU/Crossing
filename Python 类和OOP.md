Python中，一切都是对象，但却并不一定要面向对象编程。
类是Python面向对象编程的主要工具，这是一种代码定制和重用的方式。

如果想把类使用的很好，就必须有预先的规划。所以，时间有限时，更适合面向过程编程，使用模块和函数就可；而要长期开发一个产品时，更适合使用类。

#### 字典与类的比较

在程序中，字典可以记录一个实体的属性，内置函数加上自定义函数，就可以处理这些数据。

```python
# 新建一个记录实体：新建一个字典
record_dict = {}
# 往里面填充数据：增加键值对
record_dict['name'] = 'Jack'
record_dict['age'] = 24
record_dict['job'] = 'Writer'
# 读取数据
print(record_dict['name'])
```
如果用类记录数据，类对象的属性、实例对象的属性，都可以记录数据。
```python
# 新建一个记录实体：新建一个类
class Record: pass
# 往里面填充数据：增加类的属性
Record.name = 'Jack'
Record.age = 24
Record.job = 'Writer'
# 新建一个记录实体：实例化一个类。
person1 = Record()
# 往里面填充数据：增加实例的属性
person1.name = 'Jack'
person1.age = 24
person1.job = 'Writer'
# 一个类可以有很多实例，不同的实例是不同的内存空间，不同的命名空间
person2 = Record()
person2.name = 'Thomas'
person1.age = 19
person1.job = 'Justice'
```
然而，结构化地构建类，却有更多的好处：`__init__()`方法可以在实例化的时候一致性地填充实例对象的数据，类下可以添加针对实例数据进行处理的逻辑（方法）。这样，成员属性就是结构化的数据，而方法就是绑定的处理逻辑，类就是数据和逻辑组合成的包，而实例则是真正的数据。

```python
# 用结构化的方式OOP
class Person():
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    def info(self):
        return self.name, self.job
person1 = Person('Jack', 24, 'Writer')
person2 = Person('Thomas', 19, 'Justice')
print(person1.age, person2.info())
```

类是一个包，里面有很多的函数和变量名，使用并且处理内置对象类型，所以类也是一种封装逻辑和数据的方式。类是一种命名空间。
类比函数更好的地方：
- 让数据（属性）和操作（方法）区域化，有利于编写和调试。
- 继承、组合。扩展和定制简单。使得OOP编程的主要任务不是从底层开始，也不是修改原来的代码，而是在现有的类的基础上用继承和组合语法进行定制和扩展，于是催生了软件框架这个概念。而将常见的OOP结构归类，又催生了设计模式的概念。
- 多重实例：类是生成实例的工厂。一个类可以有多个实例，互不干扰。而一个模块、函数只能有一个对象。
- 运算符重载：让类的实例对象，能够截获并且响应那些在内置类型上的运算符号，比如`+`。

**对象的属性访问语法：**`object.attribute`，第一步是读取这个属性，第二步是使用属性、执行表达式。模块、函数、类的实例都是这样。当然实际使用的时候，两步一般是写在一起的。比如模块对象的属性搜索和使用：

```python
from datetime import datetime
# 属性读取
now = datetime.now
# 使用属性，执行语句
print(now().strftime('%a, %b %d %H:%M'))
import math
# 属性读取
pi = math.pi
# 使用属性，执行语句
a = 3 * pi
```

**属性继承搜索：**
在OOP中，属性搜索会比其余的对象的属性搜索会复杂一点。将`基类/超类/父类` 与 `派生类/子类/子类`  的关系用树状图表达出来，父上子下，继承时候的左右顺序对应树杈的左右顺序。一个类的实例，调用属性的时候，首先搜索对象自身，然后搜索类，再搜索父类，是从下到上从左到右地搜索，直到得到第一个属性。

每个obj.attribute属性表达式都会从下到上、从左到右地搜索继承树（实例自身，类，父类），一旦搜到就停止搜索，搜完所有类树都找不到就会引发Error。这就是OOP的核心。

类的属性是有层级的，而模块的属性是扁平没有层级的。类树中，阶层更低的属性覆盖更高的属性，所以越往下走，软件就会越特定。如果要修改现有程序的功能，不是修改原有的类，而是在此基础上继承或组合来创建新的类。

类与实例：实例带有一些数据（成员属性），而类中有很多处理的函数（方法）。
Python支持多重继承，一个类可以有多个父类。
多态是指运算的意义取决于运算对象。

类的主要用途，是用来作为命名空间。

类的实例，会继承它的类和父类的属性。

对于一个模块module来说，导入后只有一个对象（一块内存区域），而类却可以有无数个实例对象。

类通常带有函数，而实例中有成员数据；实例就像是带有数据的记录，而类的方法就是处理这些数据的程序。

类方法调用：obj.method()，实际上是 Class.method(obj)

OOP中有两种对象：

- 类对象。导入或运行模块时，class语句创建的。类对象是模块对象的一个属性。它是一种生产实例的工厂。同时还提供处理数据的程序(类里面定义的方法)和共享的数据（类变量）。
- 实例对象。obj = Aclass()语句创建的。是程序处理的实际对象。每个实例都有独立的命名空间，而且有些变量名是从类中继承而来的。

在java里，class语句定义类和类下面的数据和方法，类的成员属性都要声明（保证每个实例都有这个数据），然后在构造方法里进行初始化（保证每个实例都有正确格式的初始化数据），这种做法，类真的就是实例的模板。Python的OOP通常情况也是这样做的，但在Python里，OPP的本质是：类对象和实例对象都是一种命名空间，里面的属性是通过赋值语句动态建立的，继承就会连接命名空间，obj.attribute在实例对象和类对象里面搜索属性。既然属性是通过赋值语句而实现的，那么类对象和实例对象的属性可以很自由地变化：

```python
def show_age(self):
    print(self.age)
class AClass():
    def setValue(self, value):
        self.value = value
#### 类对象的属性，非常自由
# 1.在类定义之外，给类对象添加数据。java里违法
AClass.age = 40
# 2.在类定义之外，给类对象添加方法。java里违法
AClass.show = show_age
a_instance = AClass()
print(a_instance.age)  # 40 在 1. 里附加的数据，正常使用
a_instance.show()  # 40 在 2. 里附加的方法，正常使用
#### 实例的属性，也非常自由
# 1.在类定义之外，调用 obj.attribute 创建新的成员属性。java里违法
a_instance.name = 'a_instance'
# 2.不在构造函数里创建和初始化。java里违法
a_instance.setValue(1)
# 1 和 2 创建的成员属性都可以正常使用
print(a_instance.name, a_instance.value)
# 访问不存在的属性，AttributeError: 'AClass' object has no attribute 'money'
print(a_instance.money)
```

当然，这种在class子句之外创建类和实例属性的“硬编码”方式，会造成很多调试和维护的问题，并不推荐，只是为了说明Python OPP的原理而已。

命名空间里，包含了一个对象所有的属性，通常这是用字典来实现的（模块对象、类对象、实例对象都是这样）。

```python
print(AClass.__dict__.keys())
# dict_keys(['__module__', '__doc__', 'setValue', '__weakref__', '__dict__', 'show', 'age'])
print(a_instance.__dict__.keys())
# dict_keys(['name', 'value'])
```



```python
# 每个class语句会生成新的类对象。就像def语句一样，导入模块时创建一个对象并且赋给变量名。
# class语句的作用域，就是类对象的属性命名空间。
# 就像模块的顶层赋值语句创建模块对象的属性，类内的顶层赋值语句（包括隐性，比如def）会创建类对象的属性（类方法、成员方法、类变量）。
# 类对象的属性，每个实例都可以访问。
class Person():
    name = ""
    # 在类中，def定义的函数，通常称之为方法。
    def __init__(self, name):
        # self参数是被处理的实例的参照值，表明是“这个实例”。类可以有很多实例，要指定究竟是哪一个
        # 任何带self的操作，都是操作每个实例自己的属性。
        self.name = name
        print("init")
    def say(self):
        print(self.name)
class User(Person):  # 可以多继承，左右顺序决定属性搜索顺序
    def __init__(self,name, pwd):
        Person.__init__(self, name)  # 更直观，指定初始化Person类
        # super(User, self).__init__(name)  一次性初始化所有的父类
        self.pwd = pwd

# 每次调用类，会生成一个新的实例对象。每个实例有自己的命名空间，同时获得了类的属性。
bob = User("Bob3", '123456')
# 每次实例调用属性，首先搜索自己（成员属性），然后搜索类（方法和类变量），再搜索其他父类。
# 在继承树中从下到上从左到右地搜索，就是OOP的核心。
bob.say()
```

#### `__init__`和 self 

init不一定是必须的，但init可以结构性地新建实例。self也不一定要用单词"self"，只是必须放在第一个参数位置，但用"self"是约定俗成，你自己也好读。

```python
class A():
    def __init__(some, name):
        some.name = name
a = A('Jhon')
print(a.name)
```



## 运算符重载

- 前后双下划线的方法`__x__`是特殊钩子（也叫“magic method”）。Python 的内置类型的各种运算符，和特殊的钩子都有固定不变的映射关系。所以，每个运算符，都有这种特殊钩子来拦截、响应、实现。
- 当用户自定义的类也使用了特殊钩子，就可以用相应的运算符，并且实现自定义的运算。
- 而如果用户自定义的类，没有定义相应的特殊钩子，却使用了相应的运算符，就会引发异常。
- ​

运算符重载的意义，是让用户自定义的类模仿Python内置的数据类型，就可以像内置对象一样，一致且兼容地使用自定义类的实例，最后实现与Python的内置对象模型相集成。实际应用并不多，只有必须的时候才使用（比如数学的类需要很多数学运算），一般的类不建议使用。最多见的是构造函数`__init__()`，它的作用是初始化对象的状态。



## 一个OOP的例子

##### 版本1：类是实例的工厂。而这个版本的类，因为没有方法，是数据记录的工厂。

`__init__()`方法是特殊钩子内的一种。虽然特殊钩子的样子比较特别，但它仍然是普通的函数。

构造函数：对实例对象属性进行初始化赋值。

实例对象的属性，java叫字段，是实例对象的状态信息，是用Python基本数据类型（有时也会用到自定义的类）组成的描述性数据。

```python
class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name  # self.name是实例的属性，而参数name是函数本地变量。
        self.job = job
        self.pay = pay
if __name__ == '__main__':
    '''这里放置测试代码最好'''
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    print(bob.name, bob.pay)  # Bob Smith 0
    print(sue.name, sue.pay)  # Sue Jones 1000000
```

##### 版本2：往类里添加方法：

如果我们要对实例对象的属性进行操作，则可以在后面添加几行代码

```python
if __name__ == '__main__':
    '''这里放置测试代码最好'''
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    print(bob.name, bob.pay)  # Bob Smith 0
    print(sue.name, sue.pay)  # Sue Jones 1000000
    print(bob.name.split()[-1])  # Smith 操作self.name的数据
    sue.pay *= 1.10   # 原处修改sue实例
    print(sue.pay)  # 1100000.0 修改成功
```

但这种“硬编码”方式维护极其困难。

- 冗余：每个对象都必须复制粘贴相关的代码。
- 逻辑混乱：因为处理数据的代码可能散落在不同的地方，特别是修改实例变量的操作，会像共享引用的原地修改一样，带来一系列的问题。比如，另一个模块要给每个人计算个人所得税，而其他模块则给一个人涨工资，它们之间的执行顺序和逻辑导致修改困难。这个问题很难用函数来解决。

还是像java一样老老实实OOP吧。把操作对象数据的代码做成函数，放在类下面，称为“方法”。好处：类的方法可用于任何实例，避免冗余；操作对象的代码都在类方法里，而不是四处分散，利于维护；继承可以复用和扩展。

```python
class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def last_name(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.last_name())  # Smith 调用方法
    sue.giveRaise(0.1)   # 调用方法
    print(sue.pay)  # 1100000 修改成功
```

##### 版本3：运算符重载

在版本2中，如果要打印一个实例的信息，必须提取属性，如果直接打印对象，就会得到内存地址

```python
if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)  # Bob Smith
    print(bob)  # <__main__.Person object at 0x0089E030>
```

如果我想打印一个对象的各种数据，而不是内存地址，怎么办？







方法是附加给类的属性，是一个普通的函数对象，用途是处理类的实例。实例是调用方法的主体，会自动传递self参数给方法，告诉方法处理的是“我这个实例”而不是其他的实例。

```python
instance.method(args...)  # 用实例名调用方法，Python解释器会自动传递self参数
Class.method(instance, args...)  # 用类名调用方法，必须手动传递实例
```
