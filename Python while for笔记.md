Python语句按照顺序运行（上下左右），除非使用流程语句进行跳跃。
不用{}或者begin/end或者分号，用缩进判断逻辑，而一行的末尾就是这句语句的结尾。
空格、空行、注释都会被忽略。文档字符串（Docstring）会被忽略，但会被保存。
有人说这种语法是“所见即所得”，代码和逻辑一致。这样更容易维护和重用。

```python
a = 'spam eggs';  b = "spam eggs"
引号里面有引号
a = 'doesn\'t'  # doesn't 用 \'将单引号转义
a = "\"Yes,\" he said."
a = "doesn't"  # 或者混用单双引号
a = '"Yes," he said.'
转义字符
s = 'First line.\nSecond line.'  # 换行符
r避免转义——row字符串
s = r'C:\some\name'
翻倍和拼接
s = 3 * 'un' + 'ium'
多行字符串
a = """aaa
bbb
ccc"""
字符串跨行
a = ('aaa'
'bbb'
'ccc')
序列索引的原理，以"python"为例
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
除法的规则
```python
a = 17/3   # 5 地板除。两个int相除，返回int。
b = 17/3.0  # 5.66... 真除法。一旦出现float，就int转成float，整个运算执行float法则
c = 17//3.0  # 5.0  强制地板除。即使出现浮点数，按照float法则运算，但强制截尾
```

# 表达式
常见表达式
```
a = var  # 读取一个变量，并且赋值
function(arg)  # 调用函数
object.function(arg)  # 调用实例的一个方法
yield x**2
print(a,b,sep='')  # 打印
```

a=input()  # 如果按下Ctrl-C Ctrl-D 会引发异常。最好是try:ipnut()

##### 调用函数、返回值
注意：有些函数没有返回值，返回的是None对象，它的作用是对传入的参数对象作原处修改。
append()、sort()、reverse都是

```
alist = [1,2]
alist.append(3)  # 结果 alist = [1,2,3]
# 但是有些人不知道原处修改的函数没有返回值，最后丢失了列表对象
alist = alist.append(4)  # 结果  alist=None
```

#### 打印
有2种打印：
1. 写入文件：file.write(str) 将对象转成字符串，然后将字符串写入文件；
2. 标准输出流stdout：与标准输入流、错误流（异常跟踪）是程序启动的3种数据连接。一般打印到启动脚本的窗口，但是因为本质是sys.stdout对象，所以可以通过重定向写入文件。

Python2 与 Python3 的 print语法很不一样
- Python3，print()是一个函数，用函数参数来指定模式和功能（标准的函数调用语法）
- Python2，print是一个语句，用特定的语法来指定模式和功能（临时性的语法）

##### Python3的打印

```Python
print([object1,object2...]  [,sep=' ']  [,end='\n']  [,file=sys.stdout])
```
- object1,object2...：传入的需要打印的对象，用逗号分隔。print函数将它们传给内置str()函数，变为“用户友好”字符串。
- sep=' '：指定各个对象打印出来的间隔，默认是一个空格。
- end='\n'：指定添加在打印文本末尾的字符串，默认是换行符（也就是一个print语句会换一行）。
- file=sys.stdout：指定将输出流发送的地点（任何带有write(str)方法的文件、标准流等），默认是标准流 sys.stdout，也就是打印到屏幕。

```
a,b,c = 1,'you',['me']
print(a,b,c,sep='...',end='!\n')  # 结果 1...you...me!
```
虽然print()的sep和end参数很方便，但是最好还是自己定制一个格式：

```
text = '%s: %-.4f, %05d' % ('result', 3.1415926, 42)
print(text)  # result：3.1416,00042
```

##### Python2的打印
```
print [>> file=sys.stdout]  [object1,object2...]  [,]  [,file=sys.stdout]
```
- object1,object2...：传入的需要打印的对象，用逗号分隔。print函数将它们传给内置str()函数，变为“用户友好”字符串。
- ，加了逗号，就不会换行
- ’>> file=sys.stdout‘：指定将输出流发送的地点（任何带有write(str)方法的文件、标准流等），默认是标准流 sys.stdout，也就是打印到屏幕。

取消中间的空格，有2个方法：
- print a+b+c  # 最好别这么写
- print '%s...%s...%s' % (a,b,c)  # 推荐写法



让Python2 也能支持 print()
```
from __future__ import print_function
print(1)
print('a', 'b', 'c')  # 并不可靠，有些Python版本会打印出元组  ('a', 'b', 'c')
# 更可靠的同时打印多个对象的方式————格式化字符串，自定义格式
print(%s %s %s % ('a', 'b', 'c'))
print('{} {} {}'.format('a', 'b', 'c'))
```

#### 重定向
实际上，打印和写入文件，是对等的。
print(a,b) 和 print a,b 等价于
```
import sys
sys.stdout.write(str(a)+' '+str(b)+'\n')
```
这，就是重定向的原理。

1. 永久重定向（这次运行的整个过程都重定向）
    ```
    import sys
    sys.stdout = open('log.txt', 'a')
    # 此后，每个print语句都被重定向了。
    ```
2. 暂时性重定向（只在重定向这一次打印）.这需要一个文件对象（它有write(str)方法，而不是一个文件名字符串）
	```
	print(a,b,c,file=open(log.txt,'a'))  # 重定向语句
	print >> open(log.txt,'a'),a,b,c  # Python2语法
	```
	这就像永久重定向后，恢复正常
	```
	origin = sys.stdout
	sys.stdout = open(log.txt,'a')
	print(a,b,c)
	sys.stdout.close()
	sys.stdout = origin
	```

标准打印和重定向的原理：
- ```Python
print(a,b)  # 标准流
sys.stdout.write(str(a)+' '+str(b)+'\n')  # 标准流的原理
print(a,b,c,file=open(log.txt,'a'))  # 重定向语句
open(log.txt,'a').write(str(a)+' '+str(b)+'\n')  # 重定向的原理
print >> open(log.txt,'a'),a,b,c  # Python2语法
```





# 选择和分支————if 语句

#### 布尔运算
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

Python 没有C-like语言的 switch 语句，但是有替代方案：
**java**
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


**Python 1**  如果分支很多，将会非常冗长
```
if selector == value1: <statement1>
elif selector == value2:<statement2>
else:<statement3>
```
**Python 2**  用字典，然后取值，更简洁
```
branch = {value1:statement1,value2:statement2}
if selector in branch: branch[selector]
else: statement3  # default语句
# 优化的写法
branch.get(selector,statement3)  # get方法，如果键不存在，就取默认值
```

### 三元选择符
Python没有三元选择符，但是也可以实现。
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



<center>while循环</center>
============
## 简介
while循环是最通用的迭代结构。
```Python
    while <test>:      # 循环入口检测
        <statement 1>  # 循环体
        if <test 1>: break    # 跳出循环，也不执行else
        if <test 2>: continue # 跳过此次循环，回到 while 测试
    else:              # else可选项
        <statement 2>  # 正常退出循环（不是break），就运行
```
死循环、无限循环：
```
while True:print('Ctrl-C to stop')
```
序列，循环切片，每次切出一个元素：
```Python
    x = 'spam'
    while x:  # while x != '' 的简写。判断非空，这写法很常见
        print(x,end=' ');x=x[1:]
```
常见的“变化--计数--退出”循环：
```
    a=0; b=10
    while a<b:
        print(a, end=' '); a += 1
```
Python没有 do-while，但是也可以实现"执行一次，再循环，条件成立就退出"：
```
    while true:
        <statement>          # 执行的操作代码
        if exitTest():break  # 设置退出的条件
```
跳转语句
-    break  跳出最近所在的循环
-    continue 跳到最近所在循环的开头处，也就是while/for首行
-    一般来说，break和continue会放在if里
-    else 只在循环正常离开时才执行（没有遇到break）
-    pass 占位语句，暂时填充位置，也可以用来忽略try语句的异常，定义空类、空函数。

else是Python循环特有的结构。用处是捕捉循环体中 特殊情况引发的break 而不必设立标志位/检查项.
- 循环搜索一个列表，看看里面是否包含一个值'a'。仿照C-like语言的写法
```Python
    found = False           # 设标志位 found
    while x and not found:  # x不为空 and 没有找到
        if x[0]=='a':
            print('found it'); found=True  # 一旦找到，就执行相关动作，并且改变标志位
        x=x[1:]
    if not found: print('not found') # 判断标志位，并且执行相关操作
```
- 用Pythonic 的else就会简约很多，不必设立标志位，更为结构化。
```Python
    while x:  # x不为空 and 没有找到
        if x[0]=='a':
            print('found it'); break  # 一旦找到，就执行相关动作，然后break
        x=x[1:]
    else: print('not found') # 判断标志位，并且执行相关操作
```



C-like语言常见的“判断-处理”循环
```C
    while((x=func())!=NULL){ //对x的判断
        process(x)  //对x的处理代码
    }
```
python 不能写`while (x=func()):` 只能用以下方案替代
1. 方案1：死循环，赋值语句移到循环体中，然后 if-break
```Python
    while True:
    x = func()
    if not x: break  # 对x的判断
    process(x)  # 对x的处理代码
```
2. 方案2
```Python
    x = True
    while x:
        x = func()
        if x: process(x)
```
3. 方案3
```Python
    x = func()
    while x:
        process(x)
        x = func()
```








---
<center>for 循环</center>
============

for循环是通用的序列迭代器，可以遍历任何有序的序列对象内的元素。
语法：
```Python
    for <item> in <iterable-object>:
        <statement 1>
        if <test 1>:break
        if <test 2>:break
    else:
        <statement 2>
```
#### for循环可以遍历：
1. 序列。str、tuple、list。特别注意的是，单个元素tuple的语法。如下例
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
	`list(D.items()) # 结果为 [('a',1),('b',2),('c',3)]`
    这就是字典可以并行遍历的原因：
    ```python
    for (key, value) in D.items: print(key, ':', value)  # a:1
    ```
3. 并行遍历，用于数据库（例子待研究）。
	| 数据库 | 数据表 | 一行 | 一单元格 |
    |--------|--------|--------|--------|
    |    迭代对象    |  序列      |   元组     |   元组内的对象     |


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
只差 并行遍历。P354--P357












1












