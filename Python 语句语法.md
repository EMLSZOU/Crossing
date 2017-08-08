# Python程序执行的过程
安装好了后，IDLE (Python GUI)是命令行开发环境，可以直接写语句并且运行。
也可以用文件的形式，file-new file，写好后，保存到桌面。运行已经保存的.py文件file-open, Run-Run Module。
Python文件A.py——Python编译器编译成字节码（A.pyc/A.pyo）——Python Virtue Machine（PVM，Python解释器，虚拟机）变成二进制指令，让内存/CPU运行，运行结果
Python没有 build 和 make的步骤。
.pyc加载更快，运行无差别；.pyo，优化后的文件，运行更快，然而并不是二进制文件，所以与平台无关。这些都是通过源代码编译字节码，然后在虚拟机运行。上面是CPython，也有其他的实现方式。Jython，可以让py文件变成Java程序一样，可与Java代码集成；IronPython，可以让py文件变得像.net程序一样，可与C#代码集成
#### 交互模式

#### 模块模式：第一个Python程序：
$ python ex/ex1.py  #在命令行终端输入命令来运行 ex1.py 脚本
File "ex/ex1.py", line 3 # ex1.py 文件的第 3 行有一个错误
print "I like typing this. #这一行的内容被打印出来。 然后 Python 打印出一个 ^ (井号，caret) 符号，用来指示出错的位置。少了一个 " (双引号，double-quote) 
SyntaxError: EOL while scanning string literal #“语法错误(SyntaxError)”




# 语句语法
Python 程序的结构：程序>>模块 >> 语句（构建基本工具，函数、类等等）>>表达式（建立并处理对象）
Python的语法，就是表达式和语句，而核心就是语句————语句包含表达式，建立对象，生成新的对象，管理模块。

Python语句按照顺序运行（上下左右），除非使用流程语句进行跳跃。
不用{}或者begin/end或者分号，用缩进判断逻辑，而一行的末尾就是这句语句的结尾。
空格、空行、注释都会被忽略。文档字符串（Docstring）会被忽略，但会被保存。
有人说这种语法是“所见即所得”，代码和逻辑一致。这样更容易维护和重用。

P276    语句的种类

## 注释与文档
##### 注释
Python的注释以 # 开头，后面的文字直到行尾都算注释
```python
# 单行注释
```
多行注释，三个单引号或者双引号
```python
'''
多行注释，三对单引号，或者三对双引号
'''
```
文件开头
- Shebang (也称Hashbang)，指定Python解析器路径。
```python
#!/usr/bin/python 指定一个路径里的Python解析器
#!/usr/local/bin/python  指定一个路径里的Python解析器，系统Python自带的解析器
#!/usr/bin/env python  指出要Python2，但让系统决定路径
#!/usr/bin/env python3 指出要Python3，但让系统决定路径
```
- 指定编码，避免 ASCII 编码错误
```python
#-*-coding:utf-8 -*-
# -*- coding:cp-1252 -*-
```

##### 文档字符串`__doc__`
在模块、函数、类的顶端。Python会自动封装成为文档字符串。比如 test.py
- ```python
  #!/usr/bin/env Python3
  # -*- coding: utf-8 -*-
  """This is just a test module"""
  from platform import *
  string = 'module'
  def foo():
      """__Doc__"""
      print('run foo()',python_version())
  class Test():
      """__Doc__"""
      def __init__(self):
          print('run __init__', end='\n')
  if __name__ == '__main__':
      Test()
      foo()
      print('__main__',python_version())
  ```

之后，可以用`object.__doc__`查看。但是一般不这么做，而是用 help()函数

- ```python
  import test
  print(test.__doc__)  # 模块文档
  print(test.foo.__doc__)  # 某个函数的文档
  print(test.Test.__doc__)  # 某个类的文档
  ```

**help() 函数，在交互环境下使用**
- ```python
  # 交互模式
  >>>help('a')
  # 模块模式
  import sys
  help(sys)  # 无需print()了，dir()需要print。查看一个模块的 __doc__
  help(sys.getrefcount)  # 查看模块内一个函数的 __doc__
  help(str)  # 内置对象查看
  help(str.replace)  # 内置对象的一个函数
  ```

##### dir()函数
- 获得这类对象所有的属性列表。
```python
# 交互模式
>>>import sys
>>>dir(sys)
# 模块模式
import sys
print(dir(sys))  # 导入的模块也是一个对象
print(dir([]))  # 查看 list 的属性列表。用 dir(list)也一样
if dir(str)==dir(''):print('True')  # True 构造函数名，也可以得到同样的结果。
```

## 缩进/括号/行/空行
python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}。
Python与C/C++/Java语法不同：以冒号和缩进表示逻辑；分号、大小括号不是必需的。
为什么缩进作为语法的一部分？保证可读性。Tab和空格都可以表示缩进，但不要混用Tab与空格。缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数，缩进数的空格数不一致，会运行出错。最好是4个空格最为一个缩进（很多编辑器也是这样做的）。
Python对缩进要求非常严格。首行不能有空格。操作符两边加上空格。
- ##### 代码组
  缩进相同的一组语句构成一个代码块，我们称之代码组。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
  我们将首行及后面的代码组称为一个子句(clause)。
  复合语句：首行，嵌套。if子句。代码块。
- ##### 合行（不推荐）
```python
# 简单语句合为一行（不推荐），由分号作为语句界定符
a= 1;b=2;print(a+b)
# 复合语句合为一行（不推荐），简单句才可合并为一行，否则很难读。
if a > 0: print(a); print(b)
```
- ##### 分行
  每行最大长度79，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。
```python
# 表达式的跨行，C语言方式，不推荐。斜线自己容易忘记，别人也不容易看到。
c = 1 + \
    2
# 绝对不能这样跨行，这是语法错误
c = 1  \
    + 2
# 表达式跨行，使用括号，推荐
c = (1 +
     2)
# 列表、字典、集合之类，这类对象自身就有括号。无需再加括号
d = [1,2,
     3,4]
# 函数传参，自身也有括号。无需再加括号
print(c,
      d)
# 复合句跨行，加括号
if ( a > 1 and
     b>2):
    print(a,b)
```
- #####空行
  空行并不是Python语法的一部分，只是为了易读性。
  类和top-level函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。


## 操作符

Python 中操作符大致可以分为以下六种：运算操作符、比较操作符、逻辑操作符、位操作符、赋值操作符、成员操作符。
##### 赋值操作符
- 赋值操作符有`=`、`+=`、`-=`、`*=`、`/=`、`%=`、`**=`和`//=`：
```python
L = [1, 2, 3]
a, b, c = L	# 1 2 3 序列赋值
a, b = b, a	# 2 1 交换
```

##### 运算操作符
- 运算操作符有`+`、`-`、`*`、`/`、`//`、`%`和`**`，来看几个例子：
```python
# Python3 真除法（/对于任何数都是真除法，结果是float）
a = 21 / 12 # 1.75
a = 2 / 2 #1.0
# Python3 地板除
a = 21 // 12 # 1
# Python2 真除法（必须转成float，/才是真除法）
a = 21 / 12.0 # 1.75
a = 2/2.0  #1.0
# python2 地板除
a = 21 / 12 # 1 整数除法得到整数结果，就是地板除，和 21 // 12 一样
a =  21 // 12.0 # 1.0 出现了浮点数，就必须强制地板除。
# 取模
a = 21 % 12 # 9
#平方
a =  2 ** 5 #  32 推荐 pow(2, 5)
```
有几个内建函数也可以纳入运算操作符中：
```python
a =  abs(-3.14) # 3.14 绝对值计算
a = int('123') # 123 转成整数
a = int('0b100', base=2) #  4
a = float('123.456') #123.456 转为浮点数
a = complex(3, 4) # (3+4j) 转为复数
a = (3+4j).conjugate()	# (3-4j) 共轭复数
a = divmod(21, 12)	# (1, 9) 返回(x//y, x%y)
a = pow(2, 5) # 32 幂运算
```

##### 比较操作符
- 比较操作符有`<`、`<=`、`>`、`>=`、`==`、`!=`、`is`和`is not`：
```python
print(3.14 <= 3)# False
print(3.14 <= 3.14) # True
print(3.14 <= 3.140001)# True
print(3 < 4 < 5)	#  True 代码更加简洁
# 比较两个浮点数是否在同一区间，还可以使用
(a - b) < 1.0000001
```
- `is`与`is not`是判断两个标识符是不是引用自同一个对象：
```python
a = 5
b = 5
print(a is b) # True
print(id(a)) # 10914496
print(id(b)) # 10914496
```
以上是由于 Python 的垃圾回收机制有关，当两个对象的引用计数为零时，会触发垃圾回收。为了优化速度，小整数`[-5, 256]`和单个字符会从对象池中直接获取 Python 提前建立好的对象，这些对象不会被垃圾回收机制回收。

##### 成员操作符
- 成员操作符有`in`和`not in`，用来判断一个元素是否在一个容器中：
```python
L = [1, 2, 3]
print(4 in L) # False
```

##### 逻辑操作符
- 逻辑操作符有`and`、`or`和`not`：
```python
print(not 3.14 <= 3) # True
```

##### 位操作符
- 位操作符有`&`、`|`、`^`、`~`、`<<`和`>>`：
```python
a = 21	# 0001 0101
b = 12	# 0000 1100
c = a | b  # 29
c = a & b  # 4
c = a ^ b  # 25
c = ~a     # -22
c = a << 2 # 84
c = b >> 2 # 3
```


## 表达式
常见表达式
```python
a = var  # 赋值。读取一个变量，并且赋值
function(arg)  # 调用。调用函数
object.function(arg)  # 调用实例的一个方法
yield x**2 # 返回值
print(a,b,sep='')  # 打印
a=input()  # 如果按下Ctrl-C Ctrl-D 会引发异常。最好是try:ipnut()
```

##### 调用函数、返回值
注意：有些函数没有返回值，返回的是None对象，它的作用是对传入的参数对象作原处修改。
append()、sort()、reverse都是

```python
alist = [1,2]
alist.append(3)  # 结果 alist = [1,2,3]
# 但是有些人不知道原处修改的函数没有返回值，最后丢失了列表对象
alist = alist.append(4)  # 结果  alist=None
```

## 变量和赋值语句
**变量命名规则：**
- 语法：`（下划线或字母）+（任意数目的字母、数字、下划线）`。
- 区分大小写，简洁明了：尽量不要单独使用容易混淆的符号，如小写字母‘l’，大写字母‘O’等
- 禁止使用python保留字/关键字，不能把它们用作任何标识符名称：
```Python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
- 最好不要覆盖内置变量名，比如 open是内置函数，如果open=14，将会导致open(file)出错。如果的确覆盖了，解决如下：
```python
import builtins
open = 14
builtins.open('a.txt')
```

PEP8 的变量命名惯例：
- 变量名前后有下划线，有特殊作用。前后都有下划线的变量`__x__`，对解释器有特殊意义。
    -  `_xxx`：表示私有，不建议外部随意访问
    -  `__xxx`：私有变量
    -  `__xxx__`：特殊变量
- 模块名：尽量短小，使用全部小写的方式，可以使用下划线 module_name。
- 包命名：尽量短小，使用全部小写的方式，不可以使用下划线  packagename。
- 全局变量：local_var_name 尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是`__all__`机制；二是前缀一个下划线 _x，这样就不会被 from module import * 语句导入。
- 函数名、参数名：使用全部小写的方式，可以使用下划线 function_name   function_parameter_name 。
- 常量名：全部大写的方式，可以使用下划线  GLOBAL_VAR_NAME。
- 类名：大驼峰ClassName，模块内部使用的类前面加一个下划线   _ClassName。
- 异常类：大驼峰后标注error，比如 ExceptionError
- 类的属性（方法和变量）：使用全部小写的方式，可以使用下划线 method_name  instance_var_name。如果类的属性与关键字名字冲突，后缀加划线，尽量不要使用缩略等其他方式。继承冲突：如果父类FatherClass和子类SonClass都有属性a，为避免冲突，在父类属性前加两条下划线。比如：FatherClass.__a访问父类，而SonClass.a访问子类。
- 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前缀一条下划线_x。

**赋值语句**
Python 是动态语言，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
Python创建变量的方法很简单，变量起名，然后赋值。左值（变量名）规则参考上文，右值（对象）可以是任意的合法数据类型。最好是在每一个变量赋值加上一行注解。
首次赋值创建变量名。有些数据结构的对象也会在赋值时创建，比如字典的key。一旦赋值，变量名在表达式中使用时，就会被其所引用的对象取代。
赋值是建立将对象 的引用值存储在变量名内，而不是复制对象（内存中的存储区域）。赋值的本质，就是将变量名与对象的引用值绑定。
- 变量名在使用前  必须赋值。隐式赋值：模块导入、函数定义、类定义、for循环变量、函数参数传递。
  同一个变量可以反复赋值，而且可以是不同类型的变量。例如：
```python
miles = 100     # 整型变量。变量可以赋不同的值
miles   = 1000.0   # 浮点型变量。动态语言不限类型，一个变量可以通过赋值指向不同类型的对象
miles   = 1000       # 整型变量
miles   = "runoob"     # 字符串
# 也可以是更复杂的运算
length =  3*4
# 甚至是函数eval(input())，将输入的值变为运算值，而不是原来的字符串类型
name = eval(input())
print name
```
- 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。所以动态语言比静态语言更灵活。例如Java赋值语句如下（// 表示注释）：
```java
int a; //声明a是整数类型变量
a = 123; // 只能赋值给整数
a = "mooc"; // 错误：不能把字符串赋给整型变量
```
- 请不要把赋值语句的等号等同于数学的等号。同时，理解变量在计算机内存中的表示也非常重要。请看例子：
```python
a = 10  #Python解释器 在内存中创建了一个'10'的值；然后 在内存中创建了一个名为a的变量，并把它指向'10'
a = a+2  # 这在数学中不成立。赋值语句先计算右侧的表达式a + 2，得到结果12，再赋给变量a。由于a之前的值是10，重新赋值后，x的值变成12。
b = a   #把变量a赋值给另一个变量b，实际上是把变量b指向变量a所指向的数据
a = 20 
print b   # 结果为 12
# 当你指定一个值时，相关类型的对象就会在内存中被创建：
var1 = 1  
# 您也可以使用del语句删除单个或多个对象引用。例如：
del var
del var_a, var_b
```
- 元组、列表 赋值
```python
    a, b = 1, 2   # 元组赋值，赋值顺序：a=1，然后 b=2
    (a, b) = ('GLORY', 'glory')  # 元组赋值的本质
    [a, b] = ['GLORY', 'glory']
    a, b = b, a+b  # 右边的表达式，是提取ab的值进行运算，在赋值前执行。左边，先a赋值，然后b赋值
```
- 序列赋值————左右侧匹配，然后每次赋一个值（Python2和3通用）
```python
    # 右边可以是任何可迭代对象。左边右边的长度必须对等。
    a, b, c, d = [1, 2, 3, 4]  # a=1,b=2,c=3,d=4
    a, b, c, d = 'spam'  # a='s',b='p',c='a',d='m'
    a, b, c = range(3)  # a=0, b=1, c=2
    # 嵌套的序列赋值。高级，也少见。数据结构已知的时候，取数据非常方便。
    (a, b), c = 'sp', 'am'  # a='s', b='p', c='am'
```
- 扩展的序列赋值，与分片略有不同，但更简约，也更自然————仅仅用于Python3
```python
a, *b = 'spam'  # a='s',b=['p', 'a', 'm']  对等于 a,b='spam'[0], 'spam'[1:]
*a, b = 'spam'  # a=['s','p','a'], b='m'  对等于 a,b='spam'[:-1], 'spam'[-1]
a, *b, c = 'spam'  # a='s', b=['p','a'], c='m'
# 这与分片不太一样。分片只会产生一个分片对象。
a_str = 'spam'
a, b, c = a_str[0], a_str[1:3], a_str[3]  # a='s', b='pa', c='m'
a, b, c, *d = a_str  # a='s', b='p', c='a', d=['m']
a, b, c, d, *e = a_str  # a='s', b='p', c='a', d='m', e=[]
# 不能出现 左右不对等、也不能出现 多个星号
a, b = 'spam'  # 错误
a, *b, c, *d = 'spam'  # 错误
# 在循环中，将一个序列不停地首尾切割
l = [1, 2, 3, 4]
# 分片写法
while l:
    head, l = l[0], l[1:]
    print(head, l)  # 结果是 1 [2, 3, 4] # 2 [3, 4] # 3 [4] # 4 []
# 序列赋值写法
while l:
    head, *l = l
    print(head, l)  # 结果是 1 [2, 3, 4] # 2 [3, 4] # 3 [4] # 4 []
# 扩展序列赋值，还可以用在 for 循环
for (a, b, c) in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]: pass  # python2 python3
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: pass  # Python3
for i in [(1, 2, 3, 4), (5, 6, 7, 8)]: a, b, c = i[0], i[1:3], i[3]  # Python2
```
- 多目标赋值
```python
a = b = 'spam'  # a = 'spam', b='spam' 只有1个对象，却由2个变量共享
```
- 增强赋值运算。好处：输入更少，运行也更快。
```python
a += 'f'  # a = a+'f',结果 'spamf'
print()
```


## 输入输出（print和input）
Python2 与 Python3 的 print语法很不一样
- Python3，print()是一个函数，用函数参数来指定模式和功能（标准的函数调用语法）
- Python2，print是一个语句，用特定的语法来指定模式和功能（临时性的语法）

**Python3的打印**
```Python
print([object1,object2...]  [,sep=' ']  [,end='\n']  [,file=sys.stdout])
```
- object1,object2...：传入的需要打印的对象，用逗号分隔。print函数将它们传给内置str()函数，变为“用户友好”字符串。
- sep=' '：指定各个对象打印出来的间隔，默认是一个空格。
- end='\n'：指定添加在打印文本末尾的字符串，默认是换行符（也就是一个print语句会换一行）。
- file=sys.stdout：指定将输出流发送的地点（任何带有write(str)方法的文件、标准流等），默认是标准流 sys.stdout，也就是打印到屏幕。
```python
print （300）     # 打印整数
print('world')   #3的语法，必须加括号。Python2加上括号也可
print （1 + 2 * 3）#运算结果，结果7
print(2 > 5)  #运算结果，False
print （3e30）   #运算结果，3e+30
print （'100 + 200 =', 100 + 200）   #100 + 200 = 300 
a,b,c = 1,'you',['me']
print (a,b,c,sep='...',end='!\n')  # 结果 1...you...me!
```
虽然print()的sep和end参数很方便，但是最好还是自己定制一个格式：
```python
text = '%s: %-.4f, %05d' % ('result', 3.1415926, 42)
print (text)  # result：3.1416,00042
```

**Python2的打印**
```python
print [>> file=sys.stdout]  [object1,object2...]  [,]  [,file=sys.stdout]
```
- object1,object2...：传入的需要打印的对象，用逗号分隔。print函数将它们传给内置str()函数，变为“用户友好”字符串。
- 取消中间的空格，有2个方法：
```python
print a+b+c  # 最好别这么写
print '%s...%s...%s' % (a,b,c)  # 推荐写法
```
- ，加了逗号，就不会换行
- ’>> file=sys.stdout‘：指定将输出流发送的地点（任何带有write(str)方法的文件、标准流等），默认是标准流 sys.stdout，也就是打印到屏幕。
- 让Python2 也能支持 print()
```python
from __future__ import print_function
print(1)
print('a', 'b', 'c')  # 并不可靠，有些Python版本会打印出元组  ('a', 'b', 'c')
# 更可靠的同时打印多个对象的方式————格式化字符串，自定义格式
print(%s %s %s % ('a', 'b', 'c'))
print('{} {} {}'.format('a', 'b', 'c'))
```

**重定向**
实际上，有2种打印：
1. 写入文件：file.write(str) 将对象转成字符串，然后将字符串写入文件；
2. 标准输出流stdout：与标准输入流、错误流（异常跟踪）是程序启动的3种数据连接。一般打印到启动脚本的窗口，但是因为本质是sys.stdout对象，所以可以通过重定向写入文件。

- 打印和写入文件，是对等的。
```python
# print(a,b) 和 print a,b 等价于
import sys
sys.stdout.write(str(a)+' '+str(b)+'\n')
```
- 标准打印和重定向的原理：
```Python
print(a,b)  # 标准流
sys.stdout.write(str(a)+' '+str(b)+'\n')  # 标准流的原理
print(a,b,c,file=open(log.txt,'a'))  # 重定向语句
open(log.txt,'a').write(str(a)+' '+str(b)+'\n')  # 重定向的原理
print >> open(log.txt,'a'),a,b,c  # Python2语法
```
- 永久重定向（这次运行的整个过程都重定向）
    ```python
    import sys
    sys.stdout = open('log.txt', 'a')
    # 此后，每个print语句都被重定向了。
    ```
- 暂时性重定向（只在重定向这一次打印）.这需要一个文件对象（它有write(str)方法，而不是一个文件名字符串）
 ```python
 print(a,b,c,file=open(log.txt,'a'))  # 重定向语句
 print >> open(log.txt,'a'),a,b,c  # Python2语法
 ```
 这就像永久重定向后，恢复正常
 ```python
 origin = sys.stdout
 sys.stdout = open(log.txt,'a')
 print(a,b,c)
 sys.stdout.close()
 sys.stdout = origin
 ```

**输入input()**
```python
print "Who do you think I am?"
input("输入时的提示")   # 等待输入。
```
Python2里面有两个用来从命令行接受输入的函数：input 和 raw_input。
-  input() 接收的是一个值或变量。如果输 123，就是整数 123；你输 True，就是 bool 值 True；输了 abc，程序会认为这是一个叫做 abc 的变量，而假如你没有定义过这个变量，就会报错。输入文字，必须把文字写在引号 "" 或 '' 中。
-  raw_input()  接收的则是你输入的字符串，而不管你输的是什么内容。

Python3里这两种输入方式被合并了。它保留了 input 这个名字和 raw_input 的效果。
- input()  不管你输的是什么，程序都会认为这是字符串。
  在Py3里，如何输入一个值呢？方法是 eval()将字符串str当成有效Python表达式来求值，并返回计算结果。
  value = eval(input())


## 选择和分支————if 语句
**布尔运算**
在Python里，任何非零、非空对象都为真。数字0、空对象（[]和''之类）、None都为假。比较和相等，会在数据结构中递归运算。运算符是 and or not，而不是 && || !!。计算返回的True False对象（而不是数值）。
**if 语法**
- ```Python
  if <test1>:
    <statement1>
  elif <test2>:
    <statement2>
  else:
    <statement3>

  ```


- **Python 没有C-like语言的 switch 语句，但是有替代方案：**

  ```java
  switch (selector){
  	case value1:
          <statement1>;
  		break;
  	case value2:
          <statement2>;
  		break;
      default:
          <statement3>;
  }
  ```

- **Python **  如果分支很多，将会非常冗长
```python
if selector == value1: <statement1>
elif selector == value2:<statement2>
else:<statement3>
```
用字典，然后取值，更简洁
```python
branch = {value1:statement1,value2:statement2}
if selector in branch: branch[selector]
else: statement3  # default语句
# 优化的写法
branch.get(selector,statement3)  # get方法，如果键不存在，就取默认值
```

**三元选择符（条件表达式）**
- Python没有三元选择符，但是也可以实现。
  java
```java
a = condition ? value1 : value2
```
Python 有3中实现方式
```python
a = value1 if condition else value2
a = (value2, value1)[condition]
a = condition and value1 or value2
```

## 循环————while语句
while循环是最通用的循环结构。
```Python
while <test>:      # 循环入口检测
    <statement 1>  # 循环体
    if <test 1>: break    # 跳出循环，也不执行else
        if <test 2>: continue # 跳过此次循环，回到 while 测试
            else:              # else可选项
                <statement 2>  # 正常退出循环（不是break），就运行
```
- 死循环、无限循环：
```python
while True:print('Ctrl-C to stop')
```
- Python没有 do-while，但是也可以实现"执行一次，再循环，条件成立就退出"：
```python
while 1:  # 比 while True 要好
    <statement>          # 执行的操作代码
    if exitTest():break  # 设置退出的条件
```
- 序列，循环切片，每次切出一个元素：
```Python
x = 'spam'
while x:  # while x != '' 的简写。判断非空，这写法很常见
    print(x,end=' ');x=x[1:]
```
- 常见的“变化--计数--退出”循环：
```python
a=0; b=10
while a<b:
    print(a, end=' '); a += 1
```

**跳转语句**
-    break  跳出最近所在的循环
-    continue 跳到最近所在循环的开头处，也就是while/for首行
-    一般来说，break和continue会放在if里
-    else 只在循环正常离开时才执行（没有遇到break）
-    pass 占位语句，暂时填充位置，也可以用来忽略try语句的异常，定义空类、空函数。

**else**
else是Python循环特有的结构。用处是捕捉循环体中 特殊情况引发的break 而不必设立标志位/检查项.
- 循环搜索一个列表，看看里面是否包含一个值'a'。仿照C-like语言的写法
```Python
found = False           # 设标志位 found
while x and not found:  # x不为空 and 没有找到
    if x[0]=='a':
        print('found it'); found=True  # 一旦找到，就执行相关动作，并改变found
        x=x[1:]
        if not found: print('not found') # 判断found，并且执行相关操作
```
- 用Pythonic 的else就会简约很多，不必设立标志位，更为结构化。
```Python
while x:  # x不为空 and 没有找到
    if x[0]=='a':
        print('found it'); break  # 一旦找到，就执行相关动作，然后break
        x=x[1:]
        else: print('not found') # 判断标志位，并且执行相关操作
```
- C-like语言常见的“判断-处理”循环
```java
while((x=func())!=NULL){ //对x的判断
  process(x)  //对x的处理代码
}
```
python 不能写`while (x=func()):` 只能用以下方案替代
```Python
#方案1：死循环，赋值语句移到循环体中，然后 if-break
while True:
    x = func()
    if not x: break  # 对x的判断
    process(x)  # 对x的处理代码
#方案2
x = True
while x:
    x = func()
    if x: process(x)
#方案3
x = func()
while x:
    process(x)
    x = func()
```





## 迭代————for 语句
for循环是通用的序列迭代器，可以遍历任何有序的序列对象内的元素。
- 语法：
```Python
    for <item> in <iterable-object>:
        <statement 1>
        if <test 1>:break
        if <test 2>:break
    else:
        <statement 2>
```

1. 遍历序列。str、tuple、list。特别注意的是，单个元素tuple的语法。如下例
    ```Python
        a_tuple = ('some')  # 一定不能少这个逗号 ('some',)
        for i in a_tuple:print(i)  # 变成遍历字符串 'some' 了
    ```
    用 while 也可以写出来
    ```python
    i = 0
    while i < len(x):
    	print(x[i],end=' ')
        i += 1
    ```

2. 非序列。可迭代对象。文件、字典、SQL对象

#### 并行遍历
1. 并行遍历，赋值
 ```Python
   for (a,b) in [(1,2),(3,4),(5,6)]: print(a,b)  # 解包赋值。比如第一次 a=1;b=2
 ```
   如果不用解包赋值，也不违反语法
   ```python
   for both in [(1,2),(3,4),(5,6)]: a,b = both; print(a, b)  #之后解包，效果一样
   ```
   嵌套规则不变的数据结构，用这种方法提取数据非常快捷：
   ```python
   for ((a,b),c) in [((1,2),3), ((4,5),6), ((7,8)9)]: print(a,b,c)
   ```
   任何嵌套的序列结构都可以
   ```python
   for ((a,b),c) in [((1,2),3), ('xy',6), ([7,8]9)]: print(a,b,c)
   ```
2. 遍历字典
   简单遍历，仅仅遍历 key
 ```python
   D = {'a':1,'b':2,'c':3}
   for item in D:print(item)  # 仅仅遍历key
 ```
   用D.items()就可以转为元组：
   ```python
 list(D.items()) # 结果为 [('a',1),('b',2),('c',3)]
   ```
   这就是字典可以并行遍历的原因：
   ```python
   for (key, value) in D.items: print(key, ':', value)  # a:1
   ```
3. 并行遍历，用于数据库（例子待研究）。
| 数据库  | 数据表  | 一行   | 一单元格   |
| ---- | ---- | ---- | ------ |
| 迭代对象 | 序列   | 元组   | 元组内的对象 |
4. 并行遍历 zip() 和 map()
   zip()函数以一个或者多个可迭代对象（包括文件）为参数，然后返回一个配对元素的元组组成的列表。
   ```python
   L1 = ['a','b','c','d']; L2 = [5,6,7,8]
   L3 = list(zip(L1, L2))  # [('a',5), ('b',6) ...] zip对象是虚拟的可迭代对象。可以构建 list
   d1 = dic(zip(L1, L2))  # {'a':5, 'b':6 ...} 还可以构建字典
   for (x,y) in zip(L1, L2):  # 这里使用元组赋值，解包zip()返回的 元组-列表
   	print(x, ':', y)
   ```
   多个列表（大于2）传入 zip()，也会得到 元组-列表：
   ```python
   t1 = (1, 2, 3); t2 = (4, 5, 6); t3 = (7, 8, 9)
   L = list(zip(t1, t2, t3))  # [(1,4,7), (2,5,8), (3,6,9)]
   ```
   zip会以最短序列为准，截断元组。而 Python2.x中的map()则会用None补齐缺项，在Python3.x中，map()则成为了一个值生成器。
   ```python
   a, b = 'efg', 'hijk'
   L1 = list(zip(a, b))  # [('e','h'), ('f','i'), ('g','j')]
   # python2.x
   L2 = list(map(a,b))  # [('e','h'), ('f','i'), ('g','j'), (None, 'k')]
   # Python3.x
   L2 = list(map(ord, a)) # 'efg'一个个传入ord()，然后构建列表： [101, 102, 103]
    L2 = [ord(c) for c in a]  # 等效语句： [101, 102, 103]
   ```


#### 嵌套 for 循环
例1 看看 a_list 的元素是否在 b_list 里：
```Python
a_list = [45, 3.14]; b_list = ['a', 12, 45, 2.1]
for num in a_list:
	for itme in b_list:
    	if num==item:
        	print(num,'found'); break
        else:print(num,'not found')
```
当然内嵌的for可以用 `if num in b_list:` 代替
```Python
for num in a_list:
	if num in b_list: print(num,'found')
    else: print(num,'not found')
```
这种做法，用来求两个序列的交集，非常有用：
```python
res = []
for num in a_list:
	if num in b_list: res.append(num)
```
文件对象：
用 read() 一次完全读取，或者读取指定字符数目：
```python
file = open('test.txt','r')
print(file.read())
```
用 read() 一个个字地读取，分别用while和for实现：
```python
file = open('test.txt','r')
while True:
	char = file.read()
    if not char: break
    print(char)
for char in file.read(): print(char)  # for循环会把文件一次性加载到内存
```
用 read() 指定字符数读取
```python
file = open('test.txt', 'rb')
while True:
	chunk = file.read(10)  # 10字节为一个组
    if not chunk: break
    print(chunk)
```

用 readline() 一行行读取， while 实现
```Python
file = open('test.txt','r')
while True:
	line = file.readline()
    if not line:break
    print(line, end='')  #每行已经包含换行符，所以打印不加换行符
```



---
<center>编写循环的技巧</center>
============
while更通用，但是for更常用，运行速度也更快。所以最好是用简单快捷的for，然后再用while。
#### 重复特定的次数和间隔：range()
```python
range(*arg1, arg2, arg3)  # arg1 指定起始数，arg2 指定结束数， arg3指定步长
list(range(5))  # 指定结束数。5不在其中 [0, 1, 2, 3, 4]
list(range(2, 5))  # 指定起始数。2在其中 [2, 3, 4]
list(range(0, 10, 2))  # 指定起始和步长 [0, 2, 4, 6, 8]
```

千万别蹩脚地用 range()调用其他函数，比如，有人想获得序列索引值index
```python
x = 'some'
for index in range(len(x)):
	print(index, ':', x[i])
```
这种情况应该用 enumerate():
```Python
for (index, item) in enumerate(x):
	print(index, ':', item)
```
- 另外，enumerate()返回的是一个生成器对象，生成器有一个 __next()__方法。每次产生一个元组。还可以用在列表解析式里面
```python
e = enumerate(x)
a,b = next(e)  # a=0;b='s'
[char*i for (i,char) in enumerate(x)] # ['', 'o', 'mm', 'eee']
```

用 range(len(x)) 实现间隔跳跃（如果仅仅跳过一个，if break就可）。如下：
```python
x = 'someone'
for i in range(0, len(x), 2):
	print(i, ':', x[i],end='#')  # 0:'s'#2:'m'#4:'o'#6:'e'
```
用 enumerate() 也可以:
```Python
for (index, item) in enumerate(x):
	if index % 2 != 0:continue
	print(index, ':', item)
```
如果不要偏移值，只要步进……有更简单快捷的实现方式：步进分片
```python
x = 'someone'
for char in s[::2]: print(c)
	print(i, ':', x[i],end='#')  # 0:'s'#2:'m'#4:'o'#6:'e'
```

真正非要用 range(len(x)) 的场合，是list 的原地修改：
```Python
L = [1, 2, 3, 4]
for item in L:
	x += 1
print(x, L)  # 最终结果是 x 为 5，而 L 不变。修改失败。
for i in range(len(L)):
	L[i] += 1
print(L)  # 最终结果 [2, 3, 4, 5]，这才有效
```
如果不需要原地修改，那列表解析式更为简单高效
```python
L = [1, 2, 3, 4]
L = [x+1 for i in L]
```




