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
- 运算符重载：编写特殊的方法，在特殊的环境条件下触发这些方法并且提供特定的行为，让类的实例对象能够截获并且响应那些内置的运算符号，比如`+`。运算符重载也可以继承。

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



## OOP 例1：简单介绍继承、组合、运算符重载等语法

##### 步骤1：类是实例的工厂。而这个版本的类，因为没有方法，是数据记录的工厂。

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

##### 步骤2：往类里添加方法：

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

还是像java一样老老实实OOP吧。把操作对象数据的代码做成函数，放在类下面，称为“方法”。这就是Python的封装：把逻辑封装到接口背后。好处：类的方法可用于任何实例，避免冗余；操作对象的代码都在类方法里，而不是四处分散，利于维护；可以继承复用和扩展。

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

##### 步骤3：运算符重载

在版本2中，如果要打印一个实例的信息，必须提取属性，如果直接打印对象，就会得到内存地址

```python
if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)  # Bob Smith
    print(bob)  # <__main__.Person object at 0x0089E030>
```

如果我想打印一个对象的各种数据，而不是内存地址，怎么办？写一个`__str__()`方法，每次将一个实例对象转换为字符串的时候，都会自动运行。如果写`__repr__()`则返回的是更具体的字符串。

```python
class Person():
	...(前面几行与之前相同)
    def __str__(self):
        return '[Person: %s, job: %s, salary: %s]' % (self.name, self.job, self.pay)
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    print(bob)  # [Person: Bob Smith, job: None, salary: 0] 打印的就不再是内存地址了
    print(sue)  # [Person: Sue Jones, job: Dev, salary: 1000000]
```
##### 步骤4：用子类继承
版本3的Person类已经写完。数据和逻辑已经封装到了一个单一的、自包含的软件组件中。封装行为（而不是把数据操作零散到四处），避免了冗余，有利于维护。
从Person继承Manager类（意思是Manager几乎就像个Person一样），然后添加一些定制：涨工资的时候，加上10%的额外奖金，于是就得到了20%的增长。
- 第一个扩展方式：直接复制粘贴父类代码，然后修改。
  ```python
  class Manager(Person):
      def giveRaise(self, percent, bonus=0.1):
          self.pay = int(self.pay * (1 + percent + bonus))
  ```
  虽然这样写也可以正常运行，但是这不利于维护：万一以后涨工资的方式改变了，那Person和Manager的giveRaise()都必须修改。

- 第二个扩展方式：在调用父类的方法来实现父类逻辑
  ```python
  class Manager(Person):
      def giveRaise(self, percent, bonus=0.1):
          Person.giveRaise(self, percent + bonus)
  ```
  这样写，就把Manager类的 giveRaise拆分为两部分：涨工资的逻辑仍然由Person类实现，加上奖金的类由Manager类自己实现。这更贴近我们扩展的本意：要执行标准的加工资操作，同时要加上奖金。并且，维护难度更小了。

  方法是附加给类的属性，是一个普通的函数对象，用途是处理类的实例。实例是调用方法的主体，会自动传递self参数给方法，告诉方法处理的是“我这个实例”而不是其他的实例。用类调用方法，可以执行继承树中指定的那个类下面的方法。

  ```python
  instance.method(args...)  # 用实例名调用方法，Python解释器会自动传递self参数
  Class.method(instance, args...)  # 用类名调用方法，必须手动传递实例
  ```

  而且，如果这里写成`def giveRaise(self, percent, bonus=0.1):self.giveRaise(self, percent + bonus)`，会造成方法的循环调用。
  **在继承时的多态现象：**

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
      def __str__(self):
          return '[Person: %s, job: %s, salary: %s]' % (self.name, self.job, self.pay)
  class Manager(Person):
      def giveRaise(self, percent, bonus=0.1):
          Person.giveRaise(self, percent + bonus)
  if __name__ == '__main__':
      bob = Person('Bob Smith')
      sue = Person('Sue Jones', job='Dev', pay=1000000)
      tom = Manager('Tom Jones', 'manager', 50000)
      for obj in (bob, sue, tom):
          obj.giveRaise(percent=0.1)
          print(obj)
          # [Person: Bob Smith, job: None, salary: 0]
          # [Person: Sue Jones, job: Dev, salary: 1100000]
          # [Person: Tom Jones, job: manager, salary: 60000]
  ```
  三个对象 bob, sue, tom ，自动执行相应版本的 giveRaise 方法，这就是多态——同样的操作，对不同的对象就有不同的意义，不同的结果。

- 第三种扩展方式：新增数据或者方法，与父类完全无关。
  ```python
  class Manager(Person):
      def someThingElse(self, ...):
          pass
  ```

从上面3个例子，总结**OOP编程的继承大思路：**

- 继承，无需编写任何代码就可原封不动地使用父类的方法；
- 定制，原有的类有点不合用，需要在原类的基础上修改。如果完全从头开始写新类，原类的可用部分就会浪费，相同的逻辑就造成冗余；如果改动原类，那么以后原类就没法正常使用了；如果复制原类的代码，然后修改，也会造成冗余和维护困难。最好的方式是理清逻辑，新功能用新代码实现，而旧功能，则调用原类的方法实现。
- 新增，完全新增一个功能，和原代码几乎不相干。


##### 步骤5：继承时，定制构造函数

虽然Manager类写完了，但是构造方法仍然有冗余：既然是Manager类，实例肯定是一个manager，实例化的时候`tom = Manager('Tom Jones', 'manager', 50000)`太累赘了。用定制 giveRaise 的方式改写它。

```python
class Manager(Person):
    def __init__(self, name, pay=0):
        Person.__init__(self, name, 'manager', pay)
        # super(User, self).__init__(args...)  一次性初始化所有的父类
```

以上，OOP的步骤：

- 定义父类：需要什么数据——设计init()构造方法；需要什么数据操作逻辑——设计方法；需要什么特殊功能——运算符重载。
- 定义子类：需要增加什么数据、改变初始化逻辑——定制init()构造方法；需要更改数据操作逻辑——定制或者新增方法。

这些，都来自3个基本原则：继承树的属性查找语法、给方法传递self参数、运算符重载。

##### 步骤6：其他组织类的结构：组合（代理和聚合）

对象彼此嵌套，就是组合。

- 代理：包装一个类的对象，并且通过它可以访问特定的属性。一般是用包装类来增强被包装的对象的整个接口。包装类是控制器，负责管理操作，它可以完整实现嵌入类的接口，同时又增加自己的处理逻辑。

  代理这种语法不是很常用。如果直接控制、隐藏（包裹）一个类的某些属性，可能会比较困难，这时候用代理就会非常简洁。比如，跟踪或验证另一个对象的方法调用、类装饰器、把方法调用转给其他或者定制的逻辑、扩展内置类型等等。

  ```python
  class Person():
      def __init__(self, name, job=None, pay=0):
          self.name, self.job, self.pay = name, job, pay
      def last_name(self):return self.name.split()[-1]
      def giveRaise(self, percent):self.pay = int(self.pay * (1 + percent))
      def __str__(self):
          return '[Person: %s, job: %s, salary: %s]' % (self.name, self.job, self.pay)
  class SomeOne():
      def __init__(self, name,job, pay):
          self.person = Person(name,job, pay)
      def __getattr__(self, attr):  # 将一切属性都代理了
          return getattr(self.person, attr)
      def __str__(self):  # 代理运算符重载，必须用特殊的方式
          return str(self.person)
  if __name__ == '__main__':
      sue = SomeOne('Sue Jones', job='Dev', pay=1000000)
      print(sue.name)  # Sue Jones
      print(sue)  # [Person: Sue Jones, job: Dev, salary: 1000000]
  ```

  `__getattr__`与`getattr(obj, attr)`：

  - `__getattr__`拦截未定义（不存在）的属性查找。`getattr(obj, attr)`，就像obj.attr一样开启属性查找流程。
  - 表达式sue.name，如果SomeOne类的实例对象sue有name属性，就会按照正常的属性查找运行下去，然而它根本就没有name属性，用特殊钩子`__getattr__`就能截获这种对不存在属性的读取。而在`__getattr__()`内部，则是由内置函数`getattr(self.person, attr)`实现self.person.attr的属性读取运算的。

  `getattr(obj, attr)` 与`obj.__dict__[attr]`是不同的：

  ```python
  class Person():
      def __init__(self, name, job=None, pay=0):
          self.name, self.job, self.pay = name, job, pay
      def last_name(self):pass
  sue = Person('Sue Jones', job='Dev', pay=1000000)
  # obj.__dict__只是罗列这个对象的属性。
  print(sue.__dict__) # {'pay': 1000000, 'job': 'Dev', 'name': 'Sue Jones'} 只获得实例对象的属性
  # 就像 obj.attr那样，进行完整的属性查找流程，包括继承树的查找。
  print(getattr(sue, 'last_name'))#<bound method...>方法是类的属性，只能用getattr(obj,'attr')
  ```

- 聚合：嵌入各种类的对象

  ```python
  class Department():
      def __init__(self, *args):
          self.members = list(args)
      def addMember(self, person):
          self.members.append(person)
      def giveRaises(self, percent):
          for person in self.members:
              person.giveRaise(percent)
      def showAll(self):
          for person in self.members:
              print(person)
  if __name__ == '__main__':
      bob = Person('Bob Smith')
      sue = Person('Sue Jones', job='Dev', pay=1000000)
      tom = Manager('Tom Jones', 50000)
      devTeam = Department(bob, sue)
      devTeam.addMember(tom)
      devTeam.giveRaises(0.1)
      devTeam.showAll()
  ```

  Department是嵌入并且控制其他对象的聚合体——组合语法；Manager是Person基础上定制而成的——继承语法。

  一个类，究竟使用继承还是组合，取决于要建模的对象。一个GUI类可能继承第三方库，定制标签和按钮，但是也会用复合构建嵌入的挂件（比如输入的表单）。

##### 步骤7：使用内省工具

然而打印每个实例print(obj)却做的不好，tom应该打出Manager的，却打成了Person类。另外，以后万一把"job"属性换成了"title"岂不是又要改？问题在于Person的`def __str__(self):`，使用**内省工具**可以解决这个问题。

```python
instance.__class__  # 用实例连接到类。instance.__bases__是所有的超类的列表
class.__name__ # 类有一个__name__属性。instance.__class__.__name__就可以访问自己的类名
obj.__dict__  # 任何对象，都有一个字典，key:value是一个属性：属性值。
# 将Person的 __str__()方法改写
class Person():
	...
    def __str__(self):
        class_name = self.__class__.__name__
        attrs = [key + '=' + str(self.__dict__[key]) for key in self.__dict__]
        return '%s: %s' % (class_name, ', '.join(attrs))
```

打出来的格式就正确了。

Person: job=Dev, pay=1100000, name=Sue Jones
Manager: job=manager, pay=60000, name=Tom Jones 

如果将这个提取出来，作为一个通用的类，再放到一个模块里，提供给任何类使用，也是很好的

```python
# showclasstools.py
class AttrDisplay():  # 显示属性的工具类
    def __gatherAttrs(self): # _x 是类内隐藏方法；__x 是伪私有类属性
        attrs = ['%s=%s' % (key, getattr(self, key)) for key in self.__dict__]
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.__gatherAttrs())
```

这样，Person类就变为

```python
from showclasstools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        print('Person init start')
        self.name = name
        self.job = job
        self.pay = pay
        print('Person init over')
    def last_name(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
```

##### 步骤8：对象持久化——把对象存储到数据库中

让实例对象持久化很容易。3个相关模块：

- pickle：将内存中的任何Python对象（内置类型对象、自定义的类的实例）序列化为字符串。并且可以从字符串中恢复内存中的Python对象。
- dbm（Python2的anydbm）：创建一个用键访问的文件系统来存储字符串。
- shelve：使用另两个模块按照键把Python对象存储到一个文件中。shelve先使用pickle将对象序列化字符串，然后存储在dbm文件的键之下；载入的时候，shelve通过键获取字符串，然后用pickle恢复为对象。在shelve里面操作对象，就像操作字典：用键存储、索引，还可以用len()、in、dict.keys()等字典工具，唯一不同的是开始的时候必须打开shelve，结束后必须关闭shelve。

```python
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='Dev', pay=1000000)
    import shelve
    db = shelve.open('persondb')  # 创建persondb.bak/persondb.dat/persondb.dir三个文件
    for obj in (sue, bob):
        db[obj.name] = obj  # key可以是任何唯一的字符串，value可以是任何Python对象
    db.close()  # 存入文件中
```

实际生成的文件可能随平台而不同。存储的文件可以打开，之后可以像普通的对象那样，读取属性、调用方法……因为pickle的时候已经记录了每个对象的属性，unpickle的时候自动连接到了那个类。所以，打开shelve对象的时候，无需导入对象的类，可以自动获取属性和方法。只有在创建新实例的时候，才需要导入类。

```python
if __name__ == '__main__':
    import shelve
    db = shelve.open('persondb')
    # 像操作字典那样操作 shelve 数据库
    print(len(db))  # 2
    print(list(db.keys()))  # ['Bob Smith', 'Sue Jones']
    print(db['Bob Smith'])  # [Person: job=None, name=Bob Smith, pay=0]
    for key in db: print(key, '=>',db[key])
    for key in sorted(db): print(key, '=>',db[key])
    # 从数据库提取出一个，然后像普通的对象那样调用方法，却无需import Person类
    bob = db['Bob Smith']
    print(bob.last_name())  # Smith
```

将对象的数据更新一次，这样才能证明持久化是完全成功的。

```python
if __name__ == '__main__':
    import shelve
    db = shelve.open('persondb')
    for key in sorted(db):
        print(key, '=>', db[key]) # Sue Jones => [Person: pay=1210000, name=Sue Jones, job=Dev]
        obj = db[key]
        obj.giveRaise(0.1)
        db[key] = obj  # 用状态已经变化的对象，更新数据库存储的对象
    db.close()
    db = shelve.open('persondb')
    for key in sorted(db):
        print(key, '=>', db[key]) # Sue Jones => [Person: pay=1331000, name=Sue Jones, job=Dev]
```



## OOP 例2：继承与组合，共同构建一个复杂的类

第一个文件 emp.py，主要是用继承语法建立了几个类。**继承是"is-a"关系**。继承很像数学的集合，高层级的父类是更大的集合，而定制化的子类是子集（或者是大集合的成员）。

```python
class Employee:  # 雇员
    def __init__(self, name, salary=0):self.name, self.salary = name, salary
    def work(self):print(self.name, 'does stuff')
    def giveRaise(self, percent):self.salary = int(self.salary * (1 + percent))
    def __repr__(self):
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)
class Chef(Employee): # 厨师
    def __init__(self, name):Employee.__init__(self, name, 50000)
    def work(self):print(self.name, 'cooks food')
class Servant(Employee): # 服务生
    def __init__(self, name):Employee.__init__(self, name, 40000)
    def work(self):print(self.name, 'service customer')
class PizzaMaker(Chef):  # 做比萨的厨师
    def __init__(self, name):Chef.__init__(self, name)
    def work(self):print(self.name, 'makes pizza')
if __name__ == '__main__':
    bob = PizzaMaker('Bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.2)
    print(bob)
    for cls in (Employee,Chef, Servant, PizzaMaker):
        obj = cls(cls.__name__)
        obj.work()
```

第二个文件 pizzashop.py，主要是用继承语法建立了几个类。**组合是"has-a"关系**。组合关系不是继承那样的集合关系，而是组件关系，一个对象是其他对象的组成部分。组合类一般会提供接口（一个可以被调用的功能），而由内嵌的对象来实现。

```python
from emp import Servant, PizzaMaker
class Customer: # 顾客的类
    def __init__(self, name):self.name = name
    def order(self, server):print(self.name, 'orders from', server)
    def pay(self, server):print(self.name, 'pay bill to', server)
class Oven: # 厨具微波炉的类
    def bake(self): print('oven bakes pizza')
class Pizzeria:  # 比萨店的类
    def __init__(self):  # 比萨店有服务员、厨师、厨具
        self.server = Servant('Jhon')
        self.chef = PizzaMaker('Bob')
        self.oven = Oven()
    def order(self, customerName):  # 服务一个顾客的流程
        customer = Customer(customerName)  # 创建这个客户信息
        customer.order(self.server)  # 客户向服务员点单
        self.chef.work()  # 厨师工作
        self.oven.bake()  # 烤箱烘烤
        customer.pay(self.server)  # 顾客结账
if __name__ == '__main__':
    shop = Pizzeria()
    shop.order('Homer') # 第一个订单：顾客'Homer'点单
    print('---*' * 3)
    shop.order('Ringer') # 第二个订单：顾客'Ringer'点单
```

在这个文件中，Pizzeria类是容器：构造函数将内嵌的对象初始化，并且将它们嵌入。Pizzeria类也是控制器：在order方法里，让内嵌对象按照顺序工作，因为顾客是流动的，而服务生则是比萨店的一部分，所以每个订单都新建一个Customer对象，但是传入self.server对象。
类名最好用名词，而方法用动词。这样，类可以表示任何用一句话表达的对象和关系。

这种组合和继承结合而成的复合类，如果要将他们持久化，将最大的那个容器类的对象持久化就可以了。

```python
shop = Pizzeria()
# 存入
import pickle
pickle.dump(shop, open('shopfile.dat', 'wb'))
# 提取
obj = pickle.load(shop, open('shopfile.dat', 'rb'))
# 像以往那样使用
shop.order('Kristyn')
```



## OOP 例3：流处理器，OOP的意义

通用的流处理器函数：

```python
def processor(reader, converter, writer):
    while 1:  # 用1 比True更快
        data = reader.read() # 用读取器，读取数据
        if not data: break  # 处理完毕，或者出现异常，就终止
        data = converter(data) # 用处理器，处理数据
        writer.write(data) # 用写入器，写入数据
```

如果使用OOP，将会更强大。

```python
class Processor:
    def __init__(self, reader, writer):  # 传入读取器和写入器
        self.reader, self.writer = reader, writer  # 用组合语法嵌入
    def converter(self, data): # 转换器是抽象接口，由子类实现
        assert False, 'converter() need defined!'
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
```

使用这个类的时候，不用操心它的内部实现逻辑（父类只提供文件扫描循环），而只需关心输入如何、要怎么处理、输出什么，就在子类或者嵌入对象里面实现它。

```python
if __name__ == '__main__':
    class Upper(Processor):  # 继承实现转换器：字符串转大写字母
        def converter(self, data): return str.upper(data)
    # 1. 输出到标准流，也就是print
    import sys
    obj = Upper(open('t.txt'), sys.stdout)
    obj.process()
    # 2. 输出到文件
    Upper(open('t.txt'), open('out.txt', 'w')).process()
    # 3. 定义写入器，然后传入写入器，更改输出的方式
    class HTMLwriter:
        def write(self, line):  # 将文字嵌入到HTML标签中
            print('<pre>%s</pre>' % str.rstrip(line))
    Upper(open('t.txt'), HTMLwriter()).process()
```







其他OPP可以做的事情：

- GUI：tkinter、WxPython、PyQt
- Web：Django
- 数据库：面向对象数据库OODB（ZODB）、SQL数据库（SQLite、MySQL）、NoSQL数据库（MongoDB）
- ORM：对象关系映射器





