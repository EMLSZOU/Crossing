迭代工具包括for循环、列表解析、in成员测试、map内置函数、其他内置函数sorted、zip、enumerate、filter、reduce、sum、any/all、min/max。
可迭代对象：这个概念很新颖，但在Python中广泛应用。可迭代对象是序列概念的泛化，序列自然是可迭代对象，但是有些对象，可以按照迭代协议来运算，在迭代环境中一次产生一个结果，可以说是虚拟的序列，也算是可迭代对象。
- 比如文件对象
```Python
f = open('t.txt', 'r')
print(f.readline(), end='')  # 每次调用readline()读取一行。文件读完，返回空字符串
print(f.readline(), end='')  # 文本里已经有换行符，所以不要再换行
print(f.__next__(), end='')  # 每次调用__next__()，返回一行
print(f.next(), end='')  # 调用 next()等同于调用__next__()
print(f.__next__(), end='')  # 文件读完，__next__()会引发StopIteration异常
```

迭代协议：可迭代的对象定义了一个`__next__()`接口，调用它要么得到下一个运算结果，要么是到达末尾，引发了一个特殊的StopIteration异常来终止迭代。
任何支持迭代协议的对象都是可迭代的。而在迭代工具（比如for循环）中，本质也是调用`__next__()`获得每一次的结果，而且在得到StopIteration异常时离开。
每一个迭代语境（for循环、sum、map、sorted、any、all、list等等）都会自动触发迭代，而不用手动地使用next(x)
迭代协议的用法：
- 如果一次性地读取文件到内存，可能会造成内存崩溃：
```python
lineList = open('a.txt').readlines()
for line in lineList: pass
```
也可以用while循环，渐次读取：
```python
f = open('t.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
```
所以，读取文件的最佳方法是不用任何read()方法，而是用for，这样写最简单，并且运行速度、内存占用都最优。它没有将数据一次存入内存，并且迭代器是C语言实现的。
```python
with open('t.txt', 'r') as f:
    for line in f:  # with是特意加的。也可以 for line in open('t.txt', 'r')
        print(line,end='')  # 文本里已经有换行符，所以不要再换行
```
文件对象本身就是迭代器，自动支持next()方法。但是列表以及很多其他的内置对象，自身不是迭代器，就必须调用内置函数 iter()来启动迭代。
```python
f = open('t.txt', 'r')
print(iter(f) is f)  # True说明文件的迭代器就是文件对象本身
l = [1,2,3]
iterObject = iter(l)
print(next(iterObject))  # 每次调用next()，都是一次手动迭代的过程
while True:
    try:
        x = next(iterObject)
    except StopIteration:
        break
    print(x,end='')
```
而在for循环等迭代工具中，则把需要启动迭代的对象自动传递给 iter()函数，然后每次都自动启动迭代过程。

##### 其他可迭代对象
- 字典
```python
d = {"a": 1, "b": 2, "c": 3}
for key in d.keys(): pass  # 一般是用 keys()将key转成一个可迭代的视图对象
# keys()、values()、items()这3种视图都是可迭代对象，需要list()之类强制转化
# 这3种视图的迭代顺序，和字典的值的构建顺序相同
klist = list(d.keys())
# 直接迭代字典，那迭代的是它的key
for key in d:
    print(key, d[key])
# 如果要对字典的key进行排序，可以用sorted函数
for k in sorted(d.keys()): print(k, d[k])
for k in sorted(d): print(k, d[k])  # 最好是这种方式
for k in list(d.keys()).sort(): pass  # 错误!sort函数原地修改，返回None
```

- shelves 和 popen也是可以迭代的  *（没有找到例子）*

- range()函数。在Python3.x中，range()取代了xrange()。支持len()、索引、切片，不支持其他的序列操作，如果要强制产生一个序列，只能用list()、tuple()。另外，一个rang()对象，可以支持多个迭代器，它们迭代的时候互不干扰。
```python
r = range(5)  # range()自身不是迭代器，而是可迭代对象
# 长度，索引，切片。注意切片非常有趣
print(len(r), r[0], r[3:], sep='; ')  # 5; 0; range(3, 5)
next(r)  # TypeError: 'range' object is not an iterator
ia = iter(r)  # 第一个迭代对象
print(next(ia), next(ia))  # 0 1
ib = iter(r)  # 第二个迭代对象
print(next(ib), next(ib))  # 0 1
```
内置的数据类型，如果可以调用iter()产生一个新的迭代对象，这说明这种数据类型支持多个迭代器；而如果一个对象自身就是迭代器，那么它只有一个迭代器。如果我们编写可迭代的类，也是同样的。
- enumerate()等函数，在可迭代对象的基础上，返回一个可迭代对象






##### 迭代工具
**返回迭代对象的工具**，类似于列表解析，但更局限，因为它需要传入函数而不能使用任意的表达式。
Python3.x比Python2.x更强调迭代，range、map、zip、filter、enumerate都返回一个可迭代对象，而不是返回一个具体的值。
- map函数，把一个函数调用应用于传入的可迭代对象中的每一项，返回各项经过这个函数运算后的值。
- zip函数组合可迭代对象中的各项
- enumerate函数，返回可迭代对象中的 index 和 各项
- filter函数，返回 函数运算为真的项

它们都是作用于可迭代对象，然后返回的也是一个可迭代对象，如果要得到所有的结果，需要list()或者[ ]强迫。
```python
f = open('t.txt', 'r')
i = map(str.upper, open('t.txt'))  # map的结果是一个可迭代对象 <map object at 0x0031EB10>
upper_list = list(i)  # 强制一次性算出所有结果，然后组成一个list
i = filter(lambda x:bool(x), open('t.txt'))  # 每个用一个函数进行运算，只保留计算结果为True的值
bool_list = list(i)  #<filter object at 0x008DEED0>用list强制转为list
i = enumerate('some')  # <enumerate object at 0x00306C60>
print(list(i))  # [(0, 's'), (1, 'o'), (2, 'm'), (3, 'e')]
i = zip('some', [1, 2, 3, 4, 5])  # <zip object at 0x008C6D78>
print(list(i))  # [('s', 1), ('o', 2), ('m', 3), ('e', 4)]在最短的元素那儿截断
```




**返回一个值的工具（而不是返回可迭代对象）**
有些工具并不会返回一个可迭代对象，而是直接返回运算结果
- reduce函数，把一个函数func作用在一个序列[x1, x2, x3...]上，这个函数func必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
```python
# 为了说明reduce的含义，将def fn(x, y):return x * 10 + y改写为lambda
# 第一次传入前两个值，运算出结果，用结果与后面的值再运算，直至迭代完毕
# 结果是 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
i = reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9])  # 13579
```
- sorted()返回排序后的可迭代对象。
- sum/min 返回最大最小值
- any/all 针对每个对象进行布尔运算，all在所有的为True返回True，any在任何一个True的时候返回True
   使用迭代协议的工具，甚至包括：
- list()和tuple()，从可迭代对象构建一个新的对象
- 字符串join()，将一个子字符串放在一个可迭代对象的字符串之间
- 序列赋值。
   ```python
   a, b, c, d = open('t.txt')  # 文件有且只有4行，才能赋值，否则Error
   a , *b = open('t.txt')  # 文件不能是空的。
   # 甚至在函数调用的时候，也可以用可迭代对象，进行参数解包赋值
   def func(a, b, c, d): print(a, b, c, d)
   func(*open('t.txt'))
   ```
##### 其他的迭代主题

可迭代的函数：生成器与yield

可迭代的类：用户定义的类，通过`__iter__`和`__getitem__`运算符重载，变得可迭代，允许在任何迭代环境中使用任意的对象和操作。可迭代的类，可以实现更丰富的逻辑和数据结构选项。


# 函数章节的迭代
## 函数式编程工具
map和filter函数，是将一个操作（传入的函数对象）映射到可迭代对象中。受其启发和影响，Python最终形成了解析式（比如列表解析）。但是解析式比这些函数式编程工具更有用。
对比for循环、map、列表解析。例子：将一个字符串转成ASCII编码列表

   ```python
# ord()可以把一个字符转成ASCII编码
print(ord('n'))  # 110
# 将一个字符串的ASCII编码组成列表。1. for循环
res = []
for char in 'one':
    res.append(ord(char))
print(res)  # [111, 110, 101]
# 2. map函数，注意是函数名，而不是带括号的函数调用func()
res = list(map(ord, 'one'))  # list()不能用[]替代
# 3. 列表解析式
res = [ord(c) for c in 'one']
   ```




## 解析式

受到函数式编程工具（map、filter、reduce等）的影响，Python最终产生了更为通用的解析式（最常见的是列表解析）。
**解析式，**是在一个可迭代对象上应用一个任意的表达式，然后将结果形成一个指定的对象（序列、可迭代对象）。它比map函数更方便的地方是：可以用于任何表达式，这样就无需写lambda了，更为简洁。
for循环、列表解析，是最常见的迭代工具。性能上，解析式速度比for循环快一倍，数据量大的时候更是如此。功能上，列表解析能够实现的需求也很多。
- **基本语法：**`[expression for item in itrable]`    例子：
```python
i_list = [i for i in range(4)]  # [0, 1, 2, 3] 最简单的取值运算
square = [i**2 for i in range(4)]  # [0, 1, 4, 9]
square = list(map(lambda x: x ** 2, range(4)))
```
列表解析式`[i**2 for i in range(4)]` 由 表达式 `i**2` 和表达式 `for i in range(4)` 组成，前面的表达式使用循环变量`i`进行运算，后面的表达式是for循环，迭代结构的取值表达式，声明了循环变量`i`，也声明了迭代对象`range(4)`。注意两个表达式 有个变量名 i 是相关联的。解析式被[ ] 包围，这说明结果是一个列表。
解析式会创造一个新的对象。
等效的for语句：
```python
la = []
for x in range(4):
    la.append(x ** 2)
square = la
```
- **带if子句**`[expression for item in itrable if condition]` 先将迭代的数据过滤，再运算
```python
even = [i for i in range(4) if i % 2 == 0]  # 提取偶数[0, 2]
even = list(filter(lambda x: x % 2 == 0, range(4)))
even_square = [i ** 2 for i in range(4) if i%2==0]  # 偶数的平方[0, 4]
even_square = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(4))))
```
- **嵌套：**解析式可以嵌套任意数量的for循环，每个for循环都可以带if子句。多个数据源结合进行解析。
```
[expression
for item1 in itrable1 (if condition1)
for item2 in itrable2 (if condition2)...
]```
例子：
​```python
res = [x + y for x in [0, 1, 2] for y in [10, 20, 30]]
# 等效的for
res = []  # 结果[10, 20, 30, 11, 21, 31, 12, 22, 32]
for x in [0, 1, 2]:
    for y in [10, 20, 30]:
        res.append(x+y)
# 带if子句的嵌套
res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 != 0]
res = []  # 结果[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 != 0:
                res.append((x, y))
```

**解析式和矩阵（多维数组）**
- 使用多维数组时，列表解析非常实用。
```python
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
print(M[1], M[1][2])  # 也是用索引取值[4, 5, 6] 6
# 列表解析式取出第一竖列
# 对行数进行迭代，然后从矩阵提取一列。适合于特殊提取，比如提取偶数行
rank = [M[rowindex][1] for rowindex in [0, 1, 2]]
# 对每一行进行迭代，从一行提取一列。适合于通用提取
rank = [row[1] for row in M]  # [2, 5, 8]
# 提取对角线的值
diagonal = [M[i][i] for i in range(len(M))]  # [1, 5, 9]
diagonal = [M[i][len(M) - i - 1] for i in range(len(M))]  # [3, 5, 7]
```
- 多个矩阵混合运算。请注意得到数列和矩阵，row和col的循环层次不一样。
```python
# 每个矩阵的数对应相乘，得到新数列 [2, 4, 6, 12, 15, 18, 28, 32, 36]
mix = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
# 每个矩阵的数对应相乘，得到新矩阵 [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
mix = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
# 实质是：内层的每一列迭代构建一个数列，外层的每一行迭代构建一个数列。for循环写法如下：
res = []
for row in range(3):
    temp = []
    for col in range(3):
        temp.append(M[row][col] * N[row][col])
    res.append(temp)
```
- 解析式和列选择（比如选取数据库查询结果的某一列）
  这种用法与二维数组非常类似。Python的标准SQL数据库API返回的查询结果，一般都是tuple组成的list：列表就是数据表，tuple是行，元组中的元素就是一个个数值。
```python
table = [('Bob', 35, 'manager'), ('Jhon', 40, 'sale')]
# 提取表内所有员工的年龄。可以用for循环，但是解析式和map会更直观，更快
ages = [age for (name, age, job) in table]  # [35, 40]
ages = list(map(lambda:(name, age, job):age, table))  # 仅用于python2.x
ages = [row[1] for row in table]
ages = list(map(lambda row: row[1], table))
```

**列表解析处理文件**
- 文件也可以列表解析，结合map()对文件进行处理
```python
# 每一行去掉换行符 \n，可以用for循环，但是解析式和map更为简洁直观
f = open('t.txt', 'r')
lines = f.readlines()
print(lines) # ['Beautiful\n', 'is better\n', 'than\n', 'ugly.\n']
lines = [line.rstrip() for line in lines]
# 还可以直接readlines
lines = [line.rstrip() for line in open('a.txt').readlines()]
# ['#!/usr/bin/env python', '# -*- coding: UTF-8 -*-', 'import time', 'from selenium import webdriver']
```
- open('a.txt').readlines()一次加载到内存，不好，容易内存爆炸。直接迭代它
```Python
lines = [line.rstrip() for line in open('a.txt')]
lines = list(map(lambda line: line.rstrip(), open('a.txt')))
# 不打开文件也可以直接去掉换行符,然后再转成大写字母
lines = [line.rstrip().upper() for line in open('t.txt', 'r')]
# 每一行都切分为一个list
lines = [line.split() for line in open('t.txt', 'r')]
# [['#!/usr/bin/env', 'python'], ['#', '-*-', 'coding:', 'UTF-8', '-*-'], ['import', 'time'], ['from', 'selenium', 'import', 'webdriver']]
# 替换：将行内空格替换为！
lines = [line.replace(' ', '!') for line in open('t.txt', 'r')]
# 多个运算：是否存在某个字母，然后索引第一个字母，返回元组(Ture, 'i')组成的列表
lines = [('sys' in line, line[0]) for line in open('t.txt', 'r')]
```

**集合解析、字典解析、生成器解析**
列表解析式，修改一下外面的括号就可以转为 集合解析、字典解析、生成器解析。Python2中只有列表解析和生成器解析，没有集合和字典解析。
- 字典和集合解析式，本质上是把生成器表达式(x for x in seq)传递给构造函数set()/dict()而已，这是一个语法糖（只是人类用起来方便，但对于计算机来说没有什么本质变化）。

  ```python
  # 生成器解析式
  gen =( em for em in enumerate(open('t.txt')))
  next(gen)
  # 集合与字典解析
  set(open('t.txt'))  # 等同于 {line for line in open('t.txt')}
  dic = {index: line for index, line in enumerate(open('t.txt'))}
  ```

  但是，嵌套太多的时候，解析式会比较难读。
  易读性：for循环 > map() > 解析式
  简洁性和效率(CPU速度和内存占用)：解析式 > map() > for循环。解析式和map在底层是以C语言实现的，而for循环是PVM用字节码运行的，所以速度差异非常大。
  易用性：解析式、map都是表达式，而for是语句，所以有些地方不能使用for循环，比如lambda、列表、字典。


  ## 生成器Generator
  生成器不立即产生结果，而是在需要的时候一次返回一个结果。有两种生成器
-   生成器函数：def语句编写的普通函数，但是不用return一次返回所有的结果，而是用yield一次返回一个结果，在每个结果之间挂起和继续它们的状态。
  - 生成器解析式：类似于列表解析式，但不是一次返回一个结果列表，而是返回一个生成器对象，调用它就能一次返回一个结果。

  不一次性地构建一个列表，就能节省内存空间，并且将计算时间分散到各个结果请求。当结果是一个很大的列表，或者计算每一个时间都很长的时候，这种功能尤其有用。但实际上生成器运行的速度会更慢，所以对于非常大的运算来说是很好的选择。
  生成器都是迭代器，都是可迭代对象，支持迭代协议。
  生成器自动在生成一个值的时候挂起，保存整个本地作用域的状态，并在下一次请求的时候继续。每一次生成一个值后，控制权都返回给调用者。
  生成器也可能有一条return语句，如果出现return，它必然会在def语句块的末尾，直接终止值的生成。但这是没有必要的，任何函数退出执行的时候，引发了StopIteration异常，从而实现了迭代的终止。

  ```python
  def gensquares(n):
      for i in range(n):
          yield i ** 2
  x = gensquares(4)
  print(x)  # <generator object gensquares at 0x102180938>
  print(next(x))  # 0
  gencompre = (i ** 2 for i in range(10))
  print(gencompre) # <generator object <genexpr> at 0x102180a98>
  next(gencompre)
  # 在一个有括号的环境里，生成器解析式就没有必要使用括号了
  l = sorted(i ** 2 for i in range(10))
  ```

  ​


**扩展生成器协议:**send()和throw(type)方法（例子不清晰）

**生成器、迭代器：**

生成器（函数、解析式都是）本身就是一种迭代器，所以没有必要像列表一样使用iter()函数创建一个迭代器。另外，它不能像列表这样的可迭代对象一样，产生多个迭代器，同时进行多个迭代。
- ```python
  g = (c * 4 for c in 'Spam')
  print(iter(g) is g)  # True，说明生成器自己就是迭代器
  # 如果强制生成两个迭代器，就会互相影响——因为本质上是同一个迭代器
  Iter1 = iter(g)
  Iter2 = iter(g)
  print(next(Iter1), next(Iter2), next(Iter1)) # SSSS pppp aaaa
  # 列表之类，可以产生多个迭代器，互不影响。并且会反映出列表的原地修改
  L = [1, 2, 3, 4]
  it1, it2 = iter(L), iter(L)
  print(next(it1), next(it2), next(it1), next(it2)) # 1 1 2 2
  del L[2:]
  print(next(it1), next(it2))  # StopIteration
  ```



## 用迭代工具模拟map和zip

Python3里，zip和map函数的用法

```python
# zip()：在最短的序列处截断，生成器每次返回一个tuple
L = list(zip('abc', 'xyz123')) #[('a', 'x'), ('b', 'y'), ('c', 'z')]
# map()：一次次地将序列的值传入函数，然后yield一个结果
L = list(map(abs, [-2, -1, 0, 1, 2]))  # [2, 1, 0, 1, 2]
# map()：函数需要N个参数，就用N个序列。在最短的序列处截断
L = list(map(pow, [1, 2, 3], [2, 3, 4, 5])) # [1, 8, 81]
```

模拟Python3的map函数
- ```python
  def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(args))
    return res
  # 用列表解析替代for循环
  def mymap(func, *seqs):
      return [func(*args) for args in zip(*seqs)]
  # 真正的map()：使用yield的generator
  def mymap(func, *seqs):
      for args in zip(*seqs):
          yield func(args)
  ```

Python2和3的zip是一样的，但是Python2的map，其实是增强版的zip，会自动补全

```python
a = zip([1, 2, 3], [4, 5, 6, 7])
print a # [(1, 4), (2, 5), (3, 6)]
a = zip([1, 2, 3], [4, 5, 6, 7], ['a', 'b', 'c'])
print a # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
a = map(None, [1, 2, 3], [4, 5, 6, 7])
print a # [(1, 4), (2, 5), (3, 6), (None, 7)]
```

模拟zip和Python2的map：

- ```python
  def myzip(*seqs):
    seqs = [list(s) for s in seqs] # 将传入的序列，都转成list
    res = []
    while all(seqs): # 只要出现空list，就为False
        res.append(tuple(s.pop(0) for s in seqs))
    return res
  # 在Python2 中模拟 自动填充的map
  def mymappad(*seqs, **kargs): # python2没法keyword-only
      pad = kargs.pop('pad', None)
      if kargs: raise TypeError("Extra args: %s" % kargs)
      seqs = [list(s) for s in seqs] # 将传入的序列，都转成list
      res = []
      while any(seqs): # 所有的都为空list，就为False
          res.append(tuple((s.pop(0) if s else pad )for s in seqs))
      return res
  a = mymappad([1, 2, 3], [4, 5, 6, 7]) # [(1, 4), (2, 5), (3, 6), (None, 7)]
  # 在Python3中模拟 自动填充的map
  def mymappad(*seqs, pad=None): # python2没法keyword-only
      seqs = [list(s) for s in seqs] # 将传入的序列，都转成list
      res = []
      while any(seqs): # 所有的都为空list，就为False
          res.append(tuple((s.pop(0) if s else pad )for s in seqs))
      return res
  ```


将它们改写为yield的generator函数

```python
def myzip(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)
def mymappad(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad )for s in seqs)
```

如果使用len()来控制，而不是pop()/any()/all()来控制，就只能适用于序列，而不适用于所有的可迭代对象。
```python
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]
# 在Python2 中模拟 自动填充的map
def mymappad(*seqs, pad=None): # python2没法keyword-only
    maxlen = max(len(s) for s in seqs)
    return [tuple((s[i] if len(s)>i else pad) for s in seqs) for i in range(maxlen)]
```
如果要将它们改写为生成器，return的不是列表解析式，而是生成器解析式就可以了
```python
def myzip(*seqs):
    minlen = min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))
# 在Python2 中模拟 自动填充的map
def mymappad(*seqs, pad=None): # python2没法keyword-only
    maxlen = max(len(s) for s in seqs)
    return (tuple((s[i] if len(s)>i else pad) for s in seqs) for i in range(maxlen))
```

单次迭代，还有map在Python2和3的差别，这是影响很大的
- ```python
  def iterzip(*args):
    # 因为map在2与3中的工作方式不同，在Python3中，生成  list <map object at 0x00947270>
    iters_list = map(iter, args) # python2 [<listiterator object at 0x02726470>, <listiterator object at 0x02726490>]
    print "list",iters_list
    while iters_list:
        res = [next(i) for i in iters_list]
        yield tuple(res)
  a = iterzip([1, 2, 3], [4, 5, 6, 7])
  # 在Python2中正常工作
  print a # <generator object iterzip at 0x0290AAD0>
  for i in a: print i, # (1, 4) (2, 5) (3, 6)
  # 在Python3中，诡异无限循环。应该修改为iters_list = list(map(iter, args))
  for i in a: print(i,end=' ') # (1, 4) () () ()...
  ```






## 统计各种迭代工具的性能（耗时、内存占用）

一般来说，列表解析最快，map会随函数的不同而性能不同，而生成器则把内存需求降到了最小。但是，每种迭代的性能表现究竟如何，就需要性能分析了。
####执行内置函数的效率比较

```python
import time, sys
reps = 10000  # 重复运行多少次
repsList = range(reps) # 把range()放在运行计时之外
def timer(func, *pargs, **kargs):
    start = time.clock() #开始计时 time.time()也可。精度随操作系统而不同
    for i in repsList:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start # 结束时间减去开始时间
    return elapsed, ret

def forLoop():
    res = []
    for x in repsList:
        res.append(abs(x))
    return res
def listComp():
    return [abs(x) for x in repsList]
def mapCall():
    return list(map(abs, repsList))
def genExpr():
    return list(abs(x) for x in repsList)
def genFunc():
    def gen():
        for x in repsList:
            yield abs(x)
    return list(gen())
if __name__ == "__main__":
    print(sys.version)
    for operate in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = timer(operate)
        print('-' * 33)
        print('%-9s: %.5f => [%s...%s]'
              % (operate.__name__, elapsed, result[0], result[-1]))
```
```html
3.5.2 (Jun 26 2016, 10:47:25)[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
---------------------------------
forLoop  : 19.67708 => [0...9999]
---------------------------------
listComp : 12.28654 => [0...9999]
---------------------------------
mapCall  : 9.42848 => [0...9999]
---------------------------------
genExpr  : 15.93393 => [0...9999]
---------------------------------
genFunc  : 16.23100 => [0...9999]```
速度：map>列表解析>生成器解析>生成器函数>for循环。map在内置函数方面有很大的优势。而生成器表达式，虽然和生成器函数的结果是一样的，但是内部实现的原理很不一样。
####执行操作的效率比较
如果不是执行abs(x)这样的内置函数，而是一个普通的 x+10操作，则把代码稍微改动一下，用自定义的abs()覆盖内置的abs()函数。
​```python
def abs(x):
    return x+10
```
结果如下。速度：列表解析>map调用>生成器解析>生成器函数>for循环。
```html
---------------------------------
forLoop  : 31.83384 => [10...10009]
---------------------------------
listComp : 24.01207 => [10...10009]
---------------------------------
mapCall  : 24.13557 => [10...10009]
---------------------------------
genExpr  : 27.12141 => [10...10009]
---------------------------------
genFunc  : 27.13629 => [10...10009]
```
####计时的方法的优化
1.不同的系统，调用不同的计时器。
2.多次运行，选出最佳，就可过滤系统的性能波动。
3.可以指定运行次数。
- ```python
  import time, sys
  def timer(func, *pargs, **kargs):
    if sys.platform[:3] == 'win': # 不同的系统，不同的计时器
        timemeter = time.clock
    else: timemeter = time.time
    def showargs(*args):pass # 改为print(args)就能跟踪参数
    _reps = kargs.pop('-reps', 10000)
    showargs(func, pargs, kargs, _reps)
    repsList = range(_reps)
    start = timemeter()
    for i in repsList:
        ret = func(*pargs, **kargs)
    elapsed = timemeter() - start
    return elapsed, ret
  def best(func, *pargs, **kargs): # 多次运行，过滤系统性能波动的影响
    _reps = kargs.pop('-reps', 10000)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1 **kargs)
        if time < best: best = time
    return (best, ret)
  ```

相应的调用代码，也变为：
```python
if __name__ == "__main__": # 启动测试的代码
    print(sys.version)
    for tester in (timer, best):
        print('<%s>' % tester.__name__)
        for operate in (forLoop, listComp, mapCall, genExpr, genFunc):
            elapsed, result = timer(operate)
            print('-' * 33)
            print('%-9s: %.5f => [%s...%s]'
                  % (operate.__name__, elapsed, result[0], result[-1]))
```




迭代器阅读列表：
https://www.zhihu.com/question/20829330
http://www.cnblogs.com/huxi/archive/2011/07/01/2095931.html
http://www.cnblogs.com/huxi/archive/2011/07/14/2106863.html
并发编程
https://zhuanlan.zhihu.com/p/25377631

