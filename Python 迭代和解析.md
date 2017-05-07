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

`__next__()`接口就是迭代协议：前进就得到下一个结果，而到达末尾的时候就会引发StopIteration异常。
任何支持迭代协议的对象都是可迭代的。而在迭代工具（比如for循环）中，本质也是调用`__next__()`获得每一次的结果，而且在得到StopIteration异常时离开。
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

##### 列表解析
for循环、列表解析，是最常见的迭代工具。性能上，速度比for循环快一倍，数据量大的时候更是如此。功能上，列表解析能够实现的需求也很多。
修改一个列表的每个元素：每个都加上10
```python
l = [1, 2, 3, 4, 5]
for i in range(len(l)):  # for index,item in enumerate(l)
    l[i] += 10
print(l)  # [11, 12, 13, 14, 15]
l = [item + 10 for item in l]
print(l)  # [21, 22, 23, 24, 25]
```
就像上面的例子，解析式写在一个环境中，表示运算结果，[ ] 表示会创建一个列表；前半部分是一个表达式，使用循环变量进行运算，x+10表示每个元素都加上10；后半部分是一个for循环，声明了循环变量x，也声明了迭代对象l。
解析式会创造一个新的对象。
上例的等效for语句是：
```python
la = []
for x in l:
    la.append(x + 10)
l = la
```
文件也可以列表解析，比如
```python
# 每一行去掉换行符 \n
f = open('t.txt', 'r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
# ['#!/usr/bin/env python', '# -*- coding: UTF-8 -*-', 'import time', 'from selenium import webdriver']
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
列表解析式，也可以转为 集合解析、字典解析、生成器解析————修改一下外面的括号就可以了
```python
set(open('t.txt'))  # 等同于 {line for line in open('t.txt')}
dic = {index: line for index, line in enumerate(open('t.txt'))}
gen =( em for em in enumerate(open('t.txt')))
```





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
可迭代的类：用户定义的类，通过__iter__和__getitem__运算符重载，变得可迭代，允许在任何迭代环境中使用任意的对象和操作。

# 函数章节的迭代
**函数式编程工具**
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
**解析式，**是在一个可迭代对象上应用一个任意的表达式，然后将结果形成一个指定的对象（序列、可迭代对象）。它比map函数更方便的地方是：可以用于任何表达式，这样就无需写lambda了，更为简洁。
`[expression for item in itrable]`
```python
square = [i**2 for i in range(4)]  # [0, 1, 4, 9]
square = list(map(lambda x: x ** 2, range(4)))
```
带if子句的解析式`[expression for item in itrable if condition]`
```python
even = [i for i in range(4) if i % 2 == 0]  # 提取偶数[0, 2]
even = list(filter(lambda x: x % 2 == 0, range(4)))
even_square = [i ** 2 for i in range(4) if i%2==0]  # 偶数的平方[0, 4]
even_square = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(4))))
```
嵌套的解析式。解析式可以嵌套任意数量的for循环，每个for循环都可以带if子句
```
[expression
for item1 in itrable1 (if condition1)
for item2 in itrable2 (if condition2)...
]```
例子：
```python
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
多个矩阵混合运算。请注意得到数列和矩阵，row和col的循环层次不一样。
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
解析式和列选择（比如选取数据库查询结果的某一列）
这种用法与二维数组非常类似。Python的标准SQL数据库API返回的查询结果，一般都是tuple组成的list：列表就是数据表，tuple是行，元组中的元素就是一个个数值。
```python
table = [('Bob', 35, 'manager'), ('Jhon', 40, 'sale')]
# 提取表内所有员工的年龄。可以用for循环，但是解析式和map会更直观，更快
ages = [age for (name, age, job) in table]  # [35, 40]
ages = list(map(lambda:(name, age, job):age, table))  # 仅用于python2.x
ages = [row[1] for row in table]
ages = list(map(lambda row: row[1], table))
```
列表解析、map()与文件对象处理
```python
lines = open('a.txt').readlines()
print(lines) # ['Beautiful\n', 'is better\n', 'than\n', 'ugly.\n']
# 如果要去除行尾的\n换行符，可以用for循环，但是解析式和map更为简洁直观
lines = [line.rstrip() for line in open('a.txt').readlines()]
# open('a.txt').readlines()一次加载到内存，不好
lines = [line.rstrip() for line in open('a.txt')]
lines = list(map(lambda line: line.rstrip(), open('a.txt')))
```





但是，嵌套太多的时候，解析式会比较难读。
易读性：for循环 > map() > 解析式
简洁性和效率(CPU速度和内存占用)：解析式 > map() > for循环。解析式和map在底层是以C语言实现的，而for循环是PVM用字节码运行的，所以速度差异非常大。
易用性：解析式、map都是表达式，而for是语句，所以有些地方不能使用for循环，比如lambda、列表、字典。























