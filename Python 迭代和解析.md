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





迭代器阅读列表：
https://www.zhihu.com/question/20829330
http://www.cnblogs.com/huxi/archive/2011/07/01/2095931.html
http://www.cnblogs.com/huxi/archive/2011/07/14/2106863.html
并发编程
https://zhuanlan.zhihu.com/p/25377631
