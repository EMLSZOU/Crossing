迭代工具包括for循环、列表解析、in成员测试、map内置函数等
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
for key in d.keys():pass  # 一般是用 keys()将key转成一个list，然后迭代
# 直接迭代字典，那迭代的是它的key
for key in d:
    print(key, d[key])
```

- shelves 和 popen也是可以迭代的  *（没有找到例子）*

- range()函数和 enumerate()函数
```python
r = range(5)  # enumerate()函数也是这样使用的，但返回的是 index,item
i = iter(r)
next(i)
```

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

