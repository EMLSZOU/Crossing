
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
**return：**函数可以有return，也可以没有。return表示函数调用结束，并且作为函数的输出，将结果（一个或者一些对象）返回给调用处，没有返回值的函数默认返回None。如果函数没有return，默认在流程执行完毕的时候将控制权交回调用处。在生成器中，yield取代return。
**调用：**调用函数的语法含简单，函数名加上括号function_name()。如果要传参，则加上参数。
```python
def times(x, y):
	return x*y
print(times(3, 4))  # 12
print(times("a",3))  #“aaa”
```
多态：一个操作的意义、结果，取决于被操作对象的类型，只要这个对象满足预期的要求（扩展对象接口protocol），就能处理，如果不支持，Python就会自己检测出来，引发异常。比如times()函数，传给它不同类型的值，执行的就是不同的操作。这正是Python的核心概念。所以，Python没有必要像静态类型语言（C/C++/Java）一样强制限定数据类型。不强制限定数据类型，让Python自己在运行的时候检测类型匹配，就可以少些很多代码，这就是Python简单灵活的根本原因。
```python
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







