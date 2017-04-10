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
死循环：`while true: print('Ctrl-C to stop')`
序列，每次切出一个元素：
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
Python没有 do-while ，但是也有替代品：
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
-    pass 什么也不做。常见用途：占位。定义空类、空函数；忽略try语句的异常。

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
2. 
```Python
    x = True
    while x:
        x = func()
        if x: process(x)
```
3. 
```Python
    x = func()
    while x:
        process(x)
        x = func()
```



a=input()  # 如果按下Ctrl-C Ctrl-D 会引发异常。最好是try:ipnut()




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
    用D.items()就可以转为元组：`list(D.items()) # 结果为 [('a',1),('b',2),('c',3)]`
    这就是字典可以并行遍历的原因：
    ```python
    for (key, value) in D.items: print(key, ':', value)  # a:1
    ```
3. 并行遍历，用于数据库（例子待研究）。
	| 数据库 | 数据表 | 一行 | 一单元格 |
    |--------|--------|--------|--------|
    |    迭代对象    |  序列      |   元组     |   元组内的对象     |
3. 
4. 1

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





