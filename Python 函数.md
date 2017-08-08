
<center>函数</center>
============
一个函数就是将一些逻辑、流程、数据、语句集合在一起的部件，这样就能反复运行。
函数的作用：代码复用、减少冗余，并且也是一种设计手段————流程分解，将复杂的系统分解为可管理的部件。
函数涉及的语法：

- 函数定义  def function(a, b=1, *c):
- 返回值  return
- 变量作用域  global  nonlocal
- 迭代返回  yield
- 匿名函数  lambda
- 调用 function()

## def 、return、调用
```python
def function_name(arg1,arg2,arg3):  #首行
	statements  # 函数体
    return  # 可选的return语句
```
**def ** 是一个可执行语句，执行时创建函数对象，并且将这个函数对象赋值给一个变量名（也就是函数名）。执行前，函数是不存在的，所以def首行语句的语法错误，模块导入就会引发异常，但是函数体只能在运行的时候才能发现错误和异常。def一般写在一个模块的顶层代码（也就是没有缩进）里面，导入模块的时候就会执行；但是它可以嵌套在if、while、def等子句中，条件满足的时候执行————如果放在if else里面，不同的条件定义不同的函数，有时候是一种很好的解决方式。
函数名就是普通的变量名，引用了一个对象，还可以像普通变量名那样操作：
```python
other_name = function_name  # 函数对象赋值一个别名
other_name()  # 用别名调用函数对象
a_list = [function_name, other_name] # 保存在列表、字典等数据结构中
```
**参数：**括号内包含0或者多个参数，称为形参，它的本质是变量名。在函数调用的时候，一个个对象赋值给形参，这样就将对象（实参）传给了函数，作为函数的输入。
**return：**函数可以有return，也可以没有。return表示函数调用结束，并且作为函数的输出，将结果（一个或者一些对象）返回给调用处。在生成器中，yield取代return，每次返回一个结果，将自己的状态挂起，并且将控制权返回给调用者。如果没有return，或者有return却没有返回值，函数默认返回None。如果函数没有return，默认在流程执行完毕的时候将控制权交回调用处。没有返回值的函数，很像其他语言的“过程”，只是执行一个任务，而不需要返回结果。
要密切关注函数的返回值，比如list.sort()和list.append()没有返回值，会造成以下的错误
- ```python
  L = [1, 3, 2]
  L = L.sort() # 错误
  L = L.append(4) # 错误
  ```
  **调用：**调用函数的语法含简单，函数名加上括号function_name()。如果要传参，则加上参数。

- ```python
  def times(x, y):
  return x*y
  print(times(3, 4))  # 12
  print(times("a",3))  #“aaa”
  ```

多态：一个操作的意义、结果，取决于被操作对象的类型，只要这个对象满足预期的要求（扩展对象接口protocol），就能处理，如果不支持，Python就会自己检测出来，引发异常。比如times()函数，传给它不同类型的值，执行的就是不同的操作。这正是Python的核心概念。所以，Python没有必要像静态类型语言（C/C++/Java）一样强制限定数据类型。不强制限定数据类型，让Python自己在运行的时候检测类型匹配，就可以少些很多代码，这就是Python简单灵活的根本原因。

- ```python
  def intersect(seq1, seq2):  # 等同于 [x for x in seq1 if x in seq2]
  res = []
    for item in seq1:
    	if item in seq2:
        	res.append(item)
  return res
  s1, s2 ,L1= "abc", "bcd",['a','b','d']
  a = intersect(s1, s2) # ['b','c']
  b = intersect(s2, L1)  #['b', 'd']
  ```
  本地变量：只是在函数内可见，而且仅在函数运行时候存在的变量。在上例中，函数内创建的变量res，这是最常见的本地变量；参数seq1和seq2，是通过赋值被传入的，也是本地变量；for循环也是将一个个对象赋值给变量，item也是本地变量。

## 作用域
Python创建、改变、或者查找变量名都是在所谓的命名空间（保存变量名的地方）中进行的。作用域就是命名空间。Python的作用域是语义作用域，变量名、作用域都是在变量创建的时候生成的，变量创建的位置决定了这个变量能被访问的范围（或者说可见范围、可以使用的地方），而不是在函数调用的地方决定的。
def内的变量名只能在def内使用：
```python
X = 99
def func():
	X = "a"  # 两个X作用域不同，互不影响
```

作用域对程序维护有着重要的影响，过度使用全局作用域是非常不好的。
作用域法则有助于防止程序的变量名冲突，并且有助于函数成为更为独立的程序单元。

模块定义的是全局作用域。函数定义的是本地作用域。
- 每一个模块都是一个全局作用域（一个创建于模块文件顶层的变量的命名空间），全局作用域仅仅对这个模块有效。导入时，对于主程序来说，这模块的全局变量就是模块的一个属性。Python没有一个变量能够跨越整个工程、不同的模块，只有导入后才能使用一个模块的变量名。
- 每次调用一个函数，都创建了一个新的本地作用域。本地变量只是临时的变量名，只在函数运行的时候存在。每一个def和lambda都定义了一个新的函数，本地作用域本来也这时候定义了，但递归函数可以循环调用自身，所以本地作用域只能是运行的时候确定。
- 任何一个变量名，都只能是本地变量、全局变量、内置变量当中的一种。即使是交互模式，输入的代码也是存在一个__main__的模块中，所以也遵循变量命名规则。
- 除非特地声明global或nonlocal，在函数内部给变量赋值（包括赋值表达式、传入的参数、函数内的for循环、嵌套def和lambda、函数内的import语句）总是创建一个本地变量名（或者赋予新的值）。

LEGB原则：当需要使用一个变量名时，Python搜索作用域的顺序是：L>E>G>B，找到就会停止寻找，所有的地方找完了仍然找不到这个变量，就会报错。既然查找的顺序是这样，那么覆盖的权重和顺序也是这样。
- Local（function）：各种在函数内创建的变量名。
- Enclosing function locals：嵌套函数，在外层的函数内（可能不止一层）。嵌套函数的变量寻找是从内向外的。
```python
def outer(): # 调用outer()，能够正确print
    a = 1
    def inner():
        print(a)  # 调用了外层函数的本地变量
    inner()
```
- Global（module）：在一个模块顶层创建的变量名。在def中赋值一个全局变量（初始化创建或者再次赋值）必须声明global；在def或者lambda内引用全局变量不需要声明。
- Built-in（Python）：Python内置的变量名，保存在`__builtin__`模块中，import 然后dir(builtin)就可以查看有哪些变量名。主要有内置函数比如open、range，也有内置异常，比如SyntaxError。有两种方式使用内置变量名：直接使用，引入builtin间接使用。
```python
file = open("c:/a.txt", 'a')  # 1.直接使用内置变量名 open
import builtins
open = 1  # 内置变量名已经被覆盖，就必须用方法2
file = builtins.open("c:/a.txt", 'a')  # 2.引入builtins模块，间接使用 open
```

#### 全局变量
- global语句：在def中赋值一个全局变量（初始化创建或者再次赋值）必须声明global。使用全局变量则不需要声明。声明global后，变量查找不遵循L>E>G>B原则，而是遵循G>B原则。
```python
x, y = 1, 2
def foo():
    global z, m # global声明一个全局变量，仅仅针对变量空间进行声明
    z = x + y
    m = 'a'
foo()
print(z,'a')
```
最好不要使用全局变量，这会让相关的函数强烈耦合，很难理解数据的处理流程，导致调试、维护极其困难。如果要数据的输入输出，那最好使用参数和return/yield。
```python
x = 99  # 两个函数都对x重新赋值。只要调用顺序不同，x的值就截然不同
def func1():
    global x
    x = 'a'
def func2():
    global x
    x = []
```
更不能在不同的模块之间更改全局变量，这会让相关的模块强烈耦合，很难调试甚至会引发bug。
```python
# a.py 模块定义了一个全局变量
x = 99
# b.py 模块，引入a模块，然后修改其中的全局变量
import a
a.x = 'change'  # 这在语法上是可以做到的
```
更为合理的方式是使用accessor函数去修改另一个模块的全局变量。虽然这样的效果还是修改了别的模块的全局变量，但是更易读，更好维护。
```python
# a.py
x = 99
def set_x(new):  # 定义accessor函数
    global x
    x = new
# b.py
import a
print(a.x)
a.set_x("change") # 使用accessor函数
print(a.x)
```
全局变量和global的主要使用方式：

1. 保持状态信息，在下次调用的时候能够继续从此处开始。
```python
x = 0  # x能记录add()调用次数
def add():
    global x
    x += 1
```
2. 用一个模块定义整个工程的全局变量。
3. 多线程之间交换信息：使用全局变量作为共享内存，让并行运行的不同函数之间交换信息

- global的替代语法：全局变量，本质就是自身模块的一个属性
- ```python
  #demo.py
  var = 99
  def local():
      var = 0  # 只是一个本地变量
  def global1():
      global var  # 全局变量常规语法：global
      var += 1
  def global2():
      var = 0  # 本地变量
      import demo  # 用自身模块的变量名访问全局变量
      demo.var += 1  # 全局变量
  def global3():
      var = 0
      import sys  # 用其他的方式访问自身模块
      glob = sys.modules['demo']
      glob.var += 1
  ```

#### 嵌套函数及嵌套作用域
**最好不要滥用嵌套函数。**嵌套函数及嵌套作用域，合理使用能有很好的效果。如下例，虽然母函数运行完毕后，它的作用域已经不存在了，但返回的函数对象记住了它里面的变量值。这种功能，用OOP类的实例变量最好，但函数式编程也可以实现。
```python
def f1():
    x = 88
    def f2():  # 函数对象f2引用了f1的本地变量x，也就是记住了这个变量
        print(x)
    return f2  # 调用f1()，返回函数对象f2
function2 = f1()
function2()  # 调用函数 f2()，结果 88
##### 如果不嵌套，也可以做到，但是比较复杂
def f2(x):
    print(x)
def f1():
    x = 88
    f2(x)
```

1. 闭合函数/工厂函数。
```python
def maker(n):
    def action(x):  # 早期Python版本不能用嵌套作用域，只能通过action(x,n=n)传参
        return x**n
    return action
square = maker(2)  # 每次调用外部函数，返回了内部函数对象，却不执行内部函数
print(square(4))  # 调用内部函数的时候，记住了执行外部函数时候的情况
cube = maker(3)
print(cube(4))
```
2. lambda函数。
3. 装饰器

嵌套函数与循环变量
- 内部的函数，只是记录了**最后一次**循环的变量值。每个函数的i都是4
```python
def maker():
    acts = []
    for i in range(5): acts.append(lambda x: i ** x)
    return acts
acts = maker()  # 得到一个lambda函数构成的列表。acts[0]就提取一个函数
print(acts[0](2))  # i=0,x=2，期望值是0，然而结果却是 16
print(acts[2](2))  # i=2,x=2，期望4，结果也是 16
```
- 内部的函数，记录了**每一次**循环的变量值。**注意这个 i=i**
```python
def maker():
    acts = []
    for i in range(5): acts.append(lambda x, i=i: i ** x)
    return acts
acts = maker()
print(acts[0](2))  # i=0,x=2，期望值是0，结果是0
print(acts[2](2))  # i=2,x=2，期望4，结果4
```

#### nonlocal语句
nonlocal语句的语法如下例：
```python
def func1():
    a, b, c = 1, 2, 3 # 只在嵌套作用域中找。如果找不到（没有创建），会引发异常
    def func2():
        # a, b, c = 'abc' # 本地变量会覆盖，会引发语法警告
        nonlocal a, b, c # nonlocal声明
        a, b, c = 3, 3, 3 # 不仅可以引用，还可以修改
```
1. nonlocal声明的变量只在嵌套作用域中查找。不在全局、内置作用域中找（如果本地有，会覆盖，所以最好不要这样做）。在嵌套作用域中找不到就引发异常。
2. nonlocal声明的变量，不仅仅可以引用，还可以进行值的修改。
- 不用nonlocal，就不能记录状态信息。Python2没有nonlocal
```python
def maker(start):
    state = start
    def inner(label):
        print(label, state) # 不用nonlocal，会执行LEGB变量查找
        # state += 1  # 根本无法修改，只能引用
    return inner
```
如果使用嵌套作用域+特殊的技巧，修改不会引发异常，实际上也不能记录状态。区分两个不同的实例倒是做到了。
```python
def maker(start):
    state = start
    def inner(label, state=state):
        print(label, state)
        state += 1
    return inner
f = maker(0)
f("some")  # some 0
f("one")  # one 0
x = maker(20)
x("go")  # go 20
f("about")  # about 0
```
global、nonlocal、类的成员属性、函数附加属性都可以保持状态信息，并且可以创建多个状态不同的副本。以下是三者的对比
- nonlocal
```python
def maker(start):
    state = start
    def inner(label):
        nonlocal state
        print(label, state)
        state += 1
    return inner
f = maker(0) ##---两个函数实例，状态信息互不影响
f("some")  # some 0
f("one")  # one 1
x = maker(20)
x("go")  # go 20
f("about")  # about 2
```
- global。如果使用全局作用域，用整个模块的全局变量记录函数的运行状态，那不同的函数对象会相互影响。并不是很好。
```python
def maker(start):
    global state
    state = start
    def inner(label):
        global state
        print(label, state)
        state += 1
    return inner
f = maker(0)
f("some")  # some 0
f("one")  # one 1
x = maker(20)  # 影响到了 f()函数对象
x("go")  # go 20
f("about")  # about 21
```
- 如果使用OOP类的成员属性也是很不错的方式。类通过属性赋值，而不是通过作用域查找，使得状态信息更明确。
```python
class Maker:
    def __init__(self, start):
        self.state = start
    def __call__(self, label): # 复写__call__（），让类的实例看起来像是一个函数
        print(label,self.state)
        self.state += 1
f = Maker(0)
f("some")  # some 0 像调用一个函数那样使用类的实例
f("one")  # one 1
x = Maker(20)
x("go")  # go 20
f("about")  # about 2
```
- 还可以给函数添加属性，从而保持状态
```python
def maker(start):
    def inner(label):
        print(label, inner.state)
        inner.state += 1
    inner.state = start  # 定义了函数，然后给它添加属性
    return inner
f = maker(0)
f("some")  # some 0
f("one")  # one 1
x = maker(20)
x("go")  # go 20
f("about")  # about 2
```

#### 再看本地变量、global、nonlocal
请注意：**本地变量、作用域声明是静态检测的，而不是运行时检测的**（相当于java的声明一样）！！！在func1()中，m在声明nonlocal前赋值，就被认为是本地变量。而在func2()中，既然没有声明global，并且在def语句块中出现本地的赋值语句，就被认为是本地变量，所以print()语句使用了不存在的变量名。
- ```python
  def func1():
    m = 'b'
    def inner():
        m = 1
        nonlocal m  # SyntaxWarning: name 'm' is assigned to before nonlocal declaration
        print(m)  # 1
    inner()
  func1()
  n = 2
  def func2():
    print(n) # UnboundLocalError: local variable 'n' referenced before assignment
    n = 'a'
  func2()
  ```
  如果在赋值之前声明global或者nonlocal，那就定义为全局变量/nonlocal变量，并且一个函数内，不可能出现同名的本地变量+global变量/nonlocal变量。如果非得使用同名的本地变量和全局变量，则可以如下：

- ```python
  n = 2
  def func2():
    import __main__
    print(__main__.n) # 2
    n = 'a'
  func2()
  ```

## 参数
#### 参数传递
传参的本质是赋值，是将传入的对象赋值给形参（函数的本地变量）。引用是以指针的方式实现的，所以参数实际上是通过指针传递的。参数传递的本质，并不是拷贝传入的对象，而是共享引用。
在函数内部的参数名赋值不会影响到实参对象，只是将变量名重新引用到另一个对象。
- ```python
  def shownum(a):
  a = 10  # 重新赋值
  print(a)
  s = 'asgsfg'
  shownum(s)
  print(s) # s并没有被赋值语句而影响
  ```
  参数赋值传递，会形成一个对象的共享引用，有可变对象的原地修改问题：

- **不可变对象**，是不可以原地修改的。
```python
def f(a):
	a += 99  # 传入后，再次赋值的本质是完全引用一个新对象，而不是修改传入的对象
    return a
b = 88
f(b)
print(b)  # b的值没有任何变化
```

- **可变对象**，是可以原地修改的。传入后修改，会影响调用方。这样就不需要 return 语句了。可变参数实参对象对函数来说，既可以作为输入也可以作为输出。
```python
def change(a):
	a[0] = 'change'
b = [3, 4]
change(b)
print(b)  # ['change', 4]
```
**避免对可变对象的修改**
-   传入拷贝的对象
  ```python
   L = [1, 2]
    change(L[:])  #等同于 L_copy=L[:]; change(L_copy)
  ```
  - 在函数内拷贝对象（这种方式比较好）
  ```python
  def change(a):
  	a = a[:]
  ```
  - 使用不可变的对象（这种方式限制性太强）
  ```python
  L = (1, 2)  # 传入的对象都是不可变的。
  def change(L): pass
  # 或者在函数将对象转化为不可变的  def change(tuple(L))
  ```

模拟其他语言“通过引用进行调用”
```python
def multiple(x, y):
    x += 1
    y = [item + 2 for item in y]
    return x, y  # 本质是返回一个元组 (x, y)
a = 1; b = [1, 2]
a, b = multiple(a, b)  # 对函数的返回值，进行解包赋值。
print(a, b)
```

#### 参数匹配语法
1. 位置参数，默认情况下，参数是通过位置进行匹配的,从左到右一一匹配。调用函数时传入的对象，必须位置相同、数量一致地传递合法的参数。
```python
def intro(name, age, say):
    print("name: %s, age: %d, say:%s" % (name, age, say))
intro("Jane", 18, "Hello")  # 如果调换顺序，或者少了一个参数，就会引发error
```
而附加的参数定义、传入参数的语法，则改变了对象匹配参数名（形参）时的优先级。
2. 关键字参数，通过变量名指定一个形参接受这个对象，而不是通过位置。这样，传参的顺序就可以任意了。
```python
def intro(name, age, say):
    print("name: %s, age: %d, say:%s" % (name, age, say))
intro(name="Jane", say="Hello", age=18)  # 指定了具体的参数名，位置就不重要了
```
函数调用时，位置参数与关键字参数可以组合

- 不能为同一个形参同时指定位置实参与关键字实参
- 任何关键字实参必须位于任何位置实参之后

```python
def intro(name, age, say):
    print("name: %s, age: %d, say:%s" % (name, age, say))
intro("Jane", age=18, say="Hello")  # 混合使用 位置、关键字传参
intro(name="Jane",18, say="Hello")  # 违法！位置参数必须在最前面
intro(18, name="Jane", say="Hello")  # 虽然语法可行，但降低了易读性
intro("Jane", age=18, "Hello")  # 违法！位置参数必须在最前面
```
定义函数时，形参列表中`*`可以单独出现(但是`**`不能)。此时函数并不表示接受一个可变长度的实参列表，而是表示`*`后面的所有实参必须作为关键字实参传入
```python
def intro(name, *, age, say):
    print("name: %s, age: %d, say:%s" % (name, age, say))
intro("Jane", age=18, say="Hello")
```
3. 默认参数，函数定义时，可以为参数设定默认值，这样允许调用时传递较少的参数。参数在def语句执行时检测——也就是函数创建的时候检测，并且会保存为一个对象，附在函数对象上，成为一个属性。默认参数的值也会附在函数对象上。
    ```python
    def intro(a, b=18):
        print("name: %s, age: %d" % (a, b))
    print(intro.__code__.co_varnames) # 参数被附在函数对象上 ('a',  'b')
    intro("JaneWei")  # 对于默认实参，可以不用给它传入实参
    def func(a=1, b): pass  # 默认参数后面，不能跟随普通参数
    def func(a, b=1): pass  # 顺序只能是：普通参数、默认参数
    ```
    如果默认参数是可原地修改的对象，每次调用改变它的值，这样就能保存它的状态。这有点像C语言的静态本地函数变量。但是，Python有更好的方式在调用之间保持状态（比如使用类）。
    ```python
    def func(x=[]):
        x.append(1)
        print(x)
    func([2])  #[2, 1]
    func()  # [1]
    func()  # [1, 1]
    func()  # [1, 1, 1]
    ```
4. 可变参数（函数定义）
    定义函数的时候，以`*`开头的参数，收集任意多的多余位置参数，组成一个元组；而以`**`开头的参数，则收集任意多的关键字参数，组成一个新字典。
```python
def intro(a, *b):
    print("a:",a, "b:",b)
intro(1)  # a: 1 b: () 没有传多余的位置参数，就是空tuple
# 传入多余的各种类型参数，都被纳入tuple
intro(1, 1, [], "xxx")  # a: 1 b: (1, [], 'xxx')
# intro(1, [], "xxx", a=1) # 非法！这时候就不能用关键字传参了
def show(a,**b):
    print("a:", a, "b:", b)
show(1)  # a: 1 b: {} 没有传入多余的关键字参数，就是空dict
# 传入多余的各种类型的关键字参数，都被纳入dict
show(1, b=1, c=[], d='xxx')  # a: 1 b: {'b': 1, 'd': 'xxx', 'c': []}
# show(1, 2, [], 'xxx')  # 非法！这时候就不能用位置传参了
def mix(a,*b,**c):
    print("a:", a, "b:", b, "c:", c)
mix(1)  # a: 1 b: () c: {} 没有多余的参数，就形成空的tuple和dict
# 这样定义函数，就可以任意传入参数了。普通参数用位置匹配
mix(1, 'a', [], c='some')  # a: 1 b: ('a', []) c: {'c': 'some'}
mix( 'a', [],a=1, c='some') # 但是用普通参数用关键字传入，还是违法！！！
```
5. 可变参数解包（调用函数）
   调用函数时，可以用`*`将序列类型的实参（如tuple、list、str、set）打散，形成位置参数；而用`**`将字典实参打散，形成关键字参数
```python
def unpack(a, b, c):
    print("a:", a, "b:", b, "c:", c)
unpack(*'123')  # a: 1 b: 2 c: 3
unpack(*['a', 1, None])  # a: a b: 1 c: {1, 2}
a_set = {1, 2, 3}
unpack(*a_set)  # a: 1 b: 2 c: 3
a_dic = {'a': 1, 'b': 'one', 'c': []}
unpack(**a_dic)  # a: 1 b: one c: []
# 甚至，将二者混合使用，也是可以的！！！
unpack(*[1, 2], **{'c': 3})  # a: 1 b: 2 c: 3
```
6. Python3的keyword-only参数
   如果想定义一个函数，调用的时候，传入任意参数，同时又指定关键字参数，就非常困难。这时候，keyWord-only参数就很有用（参见模仿Python3的print函数的例子）。
   它是一种命名参数，出现在`*`参数之后，在`**`参数之前。必须使用关键字语法传递，如果不这么做，则不能传递。
```python
def keyword(a, *b, c, **d):
    print("a:", a, "b:", b, "c:", c, "d:", d)
keyword(1, 2, 3, c=5, reversed=False, set=True)
# 结果 a: 1 b: (2, 3) c: 5 d: {'reversed': False, 'set': True}
#有时 单用一个*指定后面的全是keyWord Only
def keyWordOnly(a,*,b=1,c):pass  # b和c都必须用关键字传递。b使用了默认值
keyWordOnly(1,c=3)  # 有默认值的参数可以不传参，但传参必须指定关键字
```
7. 各类参数的顺序总结：
   **函数定义时的参数类型顺序：**
```python
def func(a,b,c='c',*d,e,f='f',**g):
    pass
# a,b:为一般参数
# c:指定了默认实参
# d:为可变位置参数
# e,f:为 keyword-only参数，其中f指定了默认参数
# g:为可变关键字参数
```
调用时必须先赋值形参c，才能进入d。无法跳过c去赋值d
e,f,g调用时必须都是关键字实参
**函数调用时实参类型顺序：**
```python
func('a','b',e='e',*seq,**dic)
#seq是一个序列，它解包之后优先覆盖c，剩下的再收集成元组传给d
#dic是一个字典，它解包之后优先考虑e,f，剩下的在收集成字典传递给g
#e='e'这个关键字实参也可以位于'b'之后的任何位置
#关键字实参必须位于位置实参之后
```
例子：
```python
def func(a, b, c='c', *d, e, f='f', **g):
    print(a, b, c, d, e, f, g)
func('a', 'b', e='e', *[1, 2, 3], **{'x': 0, 'y': 1})
# 结果 a b 1 (2, 3) e f {'y': 1, 'x': 0}
```
- 通过位置分配位置参数
- 通过匹配变量名在分配关键字参数
- 额外的非关键字参数分配到 d引用的元组中
- 额外的关键字参数分配到g引用的字典中
- 默认值分配给剩下未赋值的参数

9. 参数语法的例子
   例1：模仿min()内置函数，求任意参数集合、任意对象的最小值
```python
def min1(*args):
    first = args[0] # 以min1()不传参进行调用，这里会异常
    for arg in args:
        if arg < first:
            first = arg
    return first
def min2(first, *rest):  # 以min2()不传参进行调用，这里会异常
    for arg in rest:
        if arg < first:
            first = arg
    return first
def min3(*args):
    return sorted(args)[0]  # 以min3()不传参进行调用，这里会异常
# 但是还可以优化，函数式编程，一个函数技能提取最大值也能提取最小值
def minmax(test_func,*args):
    first = args[0] # 以min1()不传参进行调用，这里会异常
    for arg in args:
        if test_func(arg, first):
            first = arg
    return first
# 调用的时候用lambda
print(minmax(lambda x, y: x < y, 1, 42, 6, 345))  # 求最小值
print(minmax(lambda x, y: x > y, 1, 42, 6, 345))  # 求最大值
```
例2：模仿set类型的内置函数，一个或者多个序列，求交集、并集
```python
def interset(*args):  # 求交集
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res
def union(*args):  # 求并集
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res
print(interset('one', 'some', 'who')) #['o']
print(union('one', 'some', 'who')) #['o', 'n', 'e', 's', 'm', 'w', 'h']
```
例3：模仿Python3的print()内置函数
实际上并没有这个必要，在Python2中，用下句，就可以直接用print()
from __future__ import print_function
```python
import sys
def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs:  # 如果有剩余的参数就要报错
        raise TypeError('extra keywords: %s' %kargs)
    output = ''
    first = True
    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False
    file.write(output + end)
print3(1, [2], 3, sep='..', end=' >\n')  # 多个参数混合类型，指定分隔符和行尾
print3()  # 空行
print3(88,name='Jhon')  # 错误的keyword参数就报错
print3('a', {}, file=sys.stderr)  # 重定向 a {}
# 用Python3的keyWord-only参数编写，传入错误的keyword参数也可以报错
def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        pass  # 其余部分与上面相同
```

## 函数高级话题
#### 聚合性与耦合性
聚合性：尽量将任务分解成为更有针对性的函数，使得每一个函数都有一个单一的、统一的目标。不要想着把所有的步骤都混合在一起。保持简单，保持简短，一个过长或者有着很深的嵌套的函数，很可能是有设计缺陷的。
耦合性：尽量让函数和其他编程组件中的外部依赖最小化，函数的自包含性越好，就越容易读懂、复用、维护。虽然函数的输入输出方式有很多，但是尽量用return语句，其次用可变参数。
- 函数的输入有：参数、全局变量、文件、流对象
- 函数内部有：本地变量、调用其他函数或者本身
- 函数的输出有：return语句、可变参数、全局变量、文件、流对象
- 慎用全局变量，只有真正必要的时候才使用。用全局变量进行函数间的通信，会引发依赖关系和计时问题。更不应该直接修改其他模块的全局变量，这会导致模块之间的耦合。
- 用可变参数的就地修改代替return语句（比如list.sort()函数的模式取代sorted()的模式），会导致函数定义和函数调用之间的各种耦合。

#### 递归函数
在函数内部，可以调用其他函数。如果一个函数在内部直接或间接地调用自身，以进行循环运算，这个函数就是递归函数。
**例1：递归求和**
```python
def mysum(l):
    print(l)  # 打印递归的每层堆栈变量
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])
print(mysum([1, 2, 3, 4]))  # 10
# [1, 2, 3, 4]
# [2, 3, 4]
# [3, 4]
# [4]
# []
```
一层层调用，一层层返回：在每一层，这个函数都递归地调用自己，最后就到了起始点，一个空list；从起始点开始返回0，之后每一层返回相加的和。对函数调用的每一个打开的层级，在运行时调用堆栈上都有自己的一个函数本地作用域的副本，这就意味着，变量`l`在每个层级都是不同的。
可以改写为熟悉的for/while循环。循环比递归调用更加简单易读，并且内存和CPU占用都更低。
```python
sum = 0
for x in l: sum += x
while l:
    sum += l[0]
    l = l[1:]
```

还有用三元表达式优化的方案。后两者可以运算符重载，不仅仅可以递归求和，还可以拼接字符串。最后一种可以用于任何可迭代对象，比如文件。
```python
def mysum(l):
    return 0 if not l else l[0] + mysum(l[1:])
def mysum(l):  # 可以用于任何使用+运算符的类型，比如字符串拼接
    return l[0] if len(l)==1 else l[0] + mysum(l[1:])
def mysum(l):
    first, *rest = l
    return first if not rest else first + mysum(rest)
print(mysum(['Hel', 'l', 'o']))  # Hello
```
**例2：上例，间接递归**
直接递归是函数调用自身，而间接递归，是两个函数相互循环调用。
```python
def mysum(l):
    if not l:return 0
    else:
        return nonempty(l)
def nonempty(l):return l[0] + mysum(l[1:])
# 三元表达式也可以改写
def mysum(l):
    return l[0] if len(l) == 1 else nonempty(l)
def nonempty(l): return l[0] + mysum(l[1:])
```

**例3：递归计算阶乘**
因为`n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n`，
所以`fact(n) =  fact(n-1) * n`，只有n=1时需要特殊处理。
```python
def myfactorial(n):
    if n == 1:
        return 1
    return n * myfactorial(n - 1)
```
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑有时不如递归清晰（也可能更简单）。但是递归在内存和CPU性能方面却更差，特别要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试计算 myfactorial(10000)。
**例4：递归处理无限结构**
有些数据没有固定的格式，如果要运算，简单的循环体是无法操作的。比如json数据，比如下例
```python
# 求一个非线性数列的和
sublist = [1, [2, [3, 4], 5], 6, [7, 8]]
def sumtree(l):
    total = 0
    for x in l:
        if not isinstance(x, list):total += x
        else: total += sumtree(x)
    return total
print(sumtree(sublist))  # 36
```
所以：简单的线性迭代，用for/while更简单、更高效，而非线性的数据结构的运算，就非得递归不可了。

#### 函数间接调用
Python的函数，和字符串、数字一样，都是对象（内存里的一块数据区域），可以像普通对象一样操作它们：赋值给变量名、组成数据结构、传递给其他函数、作为一个函数的返回值。只是函数刚好支持一个特殊的操作——调用而已。
```python
# 函数作为对象
def echo(msg):
    print(msg)
def inderect(func, arg):  # 函数对象作为参数，传入另一个函数中
    func(arg)
x = inderect  # 函数对象赋值给变量名
x(echo, 'Hello')  # Hello
# 嵌套在数据结构中，然后for循环调用
schedule = [(echo, 'Hello'), (echo, 'world!')]
for (func, arg) in schedule:
    func(arg)
# 函数对象作为一个函数的返回值
def make(label):
    def echo(msg):
        print(label, ":", msg)
    return echo
f = make('make1')
f(1)  # make1 : 1
```
#### 函数属性和注解
**函数内省工具**
一个函数，会有很多系统定义的默认属性，用dir(func_name)会返回一个很长的列表，而调用列表中每一个都会很有作用。
其中code属性有很多功能。
```python
def func():
    a = 1
    print('Hello')
print(dir(func))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', ...]
print(func.__code__) # <code object func at 0x008CF9D0, file "D:/GitbackUp/PyProject/test.py", line 66>
print(dir(func.__code__)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
print(func.__code__.co_varnames) # ('a',)
```
**自定义的属性**
函数不仅有默认的属性，还可以有用户自定义的属性。
```python
def func():
    func.count += 1
    a = 1
    print('Hello', func.count)
func.count = 0
func.count += 1
func()  # Hello 2
func()  # Hello 3
```
自定义属性可以直接把状态信息附加给函数对象，而不必使用global、nonlocal、类等复杂的技术。自定义的属性可以在函数自身和全局访问，这就像其他语言的“静态本地变量”的一种方式。属性和对象有关，而不是和作用域有关。
**函数注解**
Python在定义函数的时候，可以附加注解。注解是不起任何作用的，这些信息会收集到__annotations__字典中，函数参数名和return是字典的key，而注解值是value。注解__annotations__就是一个普通的Python对象，可以像操作一个普通字典一样操作。
另外，注解可以作为函数装饰器参数。注解只能用于def，不能用于lambda（lambda有非常多的限制）。
```python
def tri_add(a, b, c=1):
    return a + b + c
print(tri_add(1, 2, 3))  # 6
# 在头部写上注解
def tri_add(a:'intger', b:('num',2), c:float=1)->int:return a + b + c
print(tri_add.__annotations__) #{'b': ('num', 2), 'a': 'intger', 'c': <class 'float'>, 'return': <class 'int'>}
# 操作属性对象
for key in tri_add.__annotations__:print(key)
```
#### 匿名函数lambda
def语句创建一个函数对象，并且将它赋值给一个变量名。
lambda表达式创建了一个函数对象，但是它不将它赋值给一个变量名，而是返回函数对象。当然这个对象以后也可以赋值给变量名。
**语法：**`lambda arg1,arg2...argN: expression using args`
- ```python
  def tri_add(a, b, c=1):
    return a + b + c
  # 简单逻辑可以改写为lambda
  tri_add = lambda a, b, c: a + b + c
  # lambda可以有默认参数
  tri_add = lambda a, b='are', c='me': a + b + c
  # lambda像正常函数那样，传参调用
  print(tri_add('how',c='you'))  # howareyou
  ```

lambda创建的函数对象，和def创建的一样，都可以调用，而且他们遵循同样的LEGB作用域法则。

- ```python
  def make(x):
    x += 1
    return lambda y: x + y # lambda里使用了外层的变量x
  act = make(99)
  print(act(1))  # 101
  # 如果把make也改写成lambda呢？也可以调用外层的变量
  make = lambda x: (lambda y: x + y + 1)
  ```


不同之处：行内的临时函数。
- 长处：lambda是一个表达式，而不是语句。所以可以出现在def不能出现的地方，比如嵌入到数据结构、函数调用的参数中。这可带来更简洁的代码结构。
- 限制：lambda的函数体是一个表达式，而不是一个代码块，不能有复杂的逻辑和操作，甚至不能用if语句。所以，lambda只能编写简单的任务，而def用来处理更大的任务。如果要在lambda里面封装复杂逻辑，则可以使用各种替代方案。
```python
# print()的替代品
x = 1
print(x)
import sys
sys.stdout.write(str(x)+'\n')
# if...else...的替代品
if a:
    b
else:
    c
b if a else c
(a and b) or c
# 循环语句的替代品：迭代函数比如map，列表解析
for item in [1, 2, 3]: print(item)
showall = lambda x:list(map(sys.stdout.write, x))
t = showall(['a\n', 'b\n', 'c\n'])
showall = lambda x:[sys.stdout.write(str(line)) for line in x]
t = showall(['a\n', 'b\n', 'c\n'])
```
但这些技巧必须适度使用，甚至在万不得已的时候才使用，否则代码可能很难读懂。

**常见应用**
- 跳转列表jump table（函数构成的list）和行为表（函数构成的dict）。如果使用def，不仅繁琐，这么多零碎的函数名，可能造成变量名冲突。
```python
L = [lambda x: x ** 1,
     lambda x: x ** 2,
     lambda x: x ** 3, ]
for func in L: print(func(2), end=' ')  # 2 4 8
D = {'linear':lambda x: x ** 1,
    'square': lambda x: x ** 2,
     'cube':lambda x: x ** 3}
func = D.get('square')
print(func(2))  # 4
# 如果不用lambda，就必须用def创建每一个函数，然后组建数据结构
def f1(x): return x ** 1
def f2(x): return x ** 2
def f3(x): return x ** 3
L = [f1, f2, f3]
D = {'linear': f1, 'square': f2, 'cube': f3}
```
- 回调处理器
  给tkinter GUI API定义行内的回调函数。回调处理器传递一个lambda创建的函数，作为command的关键字参数。按钮的创建Button()和点击按钮的操作lambda函数放在一起。如果是用def，按钮的创建，和按钮的操作，代码一定是分离的。
```python
import sys; from tkinter import Button, mainloop
x = Button(text='press it',
           command=(lambda: sys.stdout.write('hello\n'))
           )
x.pack()
mainloop()
```

#### 函数式编程、映射（map、reduce、filter等）
函数式编程就是对序列应用一些函数的工具。对序列的每一个元素都执行某种操作，然后把结果收集起来。
**map**
例1：在Python3中，map生成的是可迭代对象，而Python2不是。
- ```python
  L = [1, 2, 3, 4]
  def increase(x): return x + 10
  L2 = list(map(increase, L)) # 用list()产生所有的值[11, 12, 13, 14]
  L2 = list(map(lambda x: x + 10, L))  # 用lambda替代def
  print(pow(3, 4))  # pow(a, b)返回 a**b。pow需要两个参数，就用两个序列
  L3 = list(map(pow, [1,2,3], [2,3,4])) #  函数需要多少个参数，就传入多少个序列。[1, 8, 81]
  ```
  它的逻辑大致如下：

- ```python
  def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res
  ```

它比列表解析式快，但是它必须传入函数，而不是任意的表达式。

**filter**
基于某个测试函数，过滤出一些元素。
- ```python
  L4 = list(filter(lambda x: x > 0, range(-3, 3)))  # [1, 2]
  ```
  内部逻辑：

```python
def myfilter(func, seq):
    res = []
    for item in seq:
        if func(item): res.append(item)
    return res
```

**reduce**
对每个元素都累积应用某个函数，一直到计算出最后的结果。
- ```python
  from functools import reduce
  i = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])  # 13579
  # 如果想使用 +-*/%等操作，用operator导入内置的操作符
  import operator
  multi = reduce(operator.mul, range(1, 6))  # 累乘5!=120
  ```

它的内部逻辑如下

```python
def myreduce(func, seq):
    total = seq[0]
    for item in seq[1:]:
        total = func(total, item)
    return total
```