判断一个collection是不是空，
```python
if a == '' or a == None: pass # 最好不要用
if not a: pass # 而是直接布尔运算
```
三大类型：同在一个类别的类型，操作有很多共同之处。
- 数字：整数、浮点数、复数、分数。支持加减乘除等等
- 序列：字符串、列表、元组。支持索引、分片、拼接、重复。
- 映射：字典。通过键进行索引。
- 集合set是额外的类型。

可变与不可变类型：
不可变类型：数字、字符串、元组、不可变集合。不可变类型有一种完整性，保证这个对象不会被程序的其他代码改变。
可变类型：列表、字典、可变集合。可变对象可以直接在原地修改。


## 字符串
##### 字符串的创建（常量表达）
- 定义一个`a='python'`语句，它在计算机中的执行顺序是先在内存中创建一个字符串`python`，在程序栈寄存器中创建一个变量`a`，最后把`python`的地址赋给`a` 。
```python
s = "" # 空字符串。
# 单引号和双引号的意义是一样的
a = 'spam eggs'
b = "spam eggs"
# 字符串跨行（不是多行字符串，只是为了替代换行符而已）
a = ('aaa'
'bbb'
'ccc')
# 引号里面有引号
a = 'doesn\'t'  # doesn't 用 \'将引号转义
a = "\"Yes,\" he said."
a = "doesn't"  # 或者混用单双引号
a = '"Yes," he said.'  # "Yes," he said.
# 反斜杠\加上一些符号，代表特殊的字节编码——转义序列
s = 'First line.\nSecond line.'  # 换行符
# r或R避免转义——row字符串
s = r'C:\some\name'
# 多行字符串，三重引号（三重引号也会用作文档字符串、块注释）
string = '''how
are
you'''
string = 'how \n are \n you' # 多行字符串的等效形式
# Unicode字符串（Python2）
a = u"this is an unicode string"
```
转义字符
| \n | \r |\r\n| \v     | \f     |\\\|\'和\"|
|----|----|----|----|----|----|----|----|
|换行 |返回|    |垂直制表符|水平制表符|\| ' 和 "  |
Windows文件路径是用\表示的，所以有时候需要避免转义
```python
x = 'C:\picture\code' # 没有合法的转义字符，就无需避免转义
x = 'C:\\new\\a.txt' # 有合法的转义字符，就必须避开
x = r'C:\new\a.txt' # row字符串在文件路径、正则表达式中很常见
```

##### 序列操作
序列：包含其他对象的有序集合，通过位置索引。序列：Str/List/Tuple
映射：包含其他对象的无序集合，通过键索引。映射：dict
for循环是迭代操作。for循环、列表解析（本质也是for循环），是通用的迭代工具，遵循迭代协议。迭代协议：一个内存中的序列、或一个迭代操作中，每次都产生一个元素。
列表解析、map、filter 比 for循环快很多，但Python 程序优先考虑简单和可读性，其次再考虑优化和性能，所以最广泛的还是for循环。
字符串是由很多’单字符串’构成的序列。字符串是一个有序的字符的集合。Python没有C-like的char单字符类型，字符串的基本组成是单个字符‘单字符串’。
- 字符串支持**通用的序列操作**：
    1. 索引和分片。注意，绝对不能越界。
    ```python
    s = "python"
    # 索引访问。读取一个值
    print s[0] # 正向索引index，从左至右
    print s[-1] # 反向索引，从右至左，相当于 s[len(s)-1]
    #切片。得到一个新的字符串对象
    s[ M : N ], s[slice(M, N)]  切片，在序列 s 中，取出偏移量为M，直到但不包括偏移量为 N 的内容，最后得到一个新对象
    # 常见切片
    s[1:]    # 去除首位
    s[:-1]   # 去除末位。负数-n的索引，是len(s)-n的意思。
    s[:]    # 完整复制
    s[i:j:k] # 步进切片。i:j是普通切片，而k是步进值。
    s[1:10:2] # 得到13579这5个索引值的元素
    s[::2] # 得到整个序列每隔一个元素的集合
    s[::-1]  # 将整个序列反转 'nohtyp'
    li = [1, 2, 3]
    li[::-1]  # list也一样。[3, 2, 1]
    # 索引的原理。位置是“从哪儿切下”，索引是取切口右侧的元素，而切片是取切下的区间的元素。
         +---+---+---+---+---+---+
         | P | y | t | h | o | n |
         +---+---+---+---+---+---+
         0   1   2   3   4   5   6
        -6  -5  -4  -3  -2  -1
    ```
    2. 重复和拼接
    字符串拼接：见官方 Doc
	不可变性：字符串／元组／数字创建后就不可变，而列表和字典可变。
    ```python
    s = 3 * 'un' + 'ium'
    s = ‘something’
	s = ‘do ’ + s   # 变量 s 的确变为 ‘do something’, 但这是形成新的字符串对象，引用赋予变量s
    ```
	3. 计算长度、最大最小值、计数、推算索引值
	```python
    len(s) #计算出长度
    min(s); max(s) # 序列s内的最大最小值
	s.index(x[, i[, j]])
	s.count(x) # s序列内，有多少个x
    ```
    4. 迭代、in成员测试
    ```python
    'p' in s # True
    for item in s: print(item)
    ```

##### 字符串特定的操作
**字符串转换工具**
- ```python
a = '42' + 1 # 语法错误 TypeError。字符串不能和非字符串拼接。需要转成字符串，才能进行字符串的相关操作
a = '42' + str(1)  # str()将对象转为字符串，int('42')将字符串转为整数
a = '42' + str(3.14) # float('3.14') 将字符串转为浮点数
a = bin(13) # '0b1101' 算出对应的二进制，再转为字符串。互转 int('1101', 2)
num = ord('s') # 115 算出字母s的ASCII码
char = chr(115) # 's' 用ASCII码算出对应的字母
# 二者结合，可以用字符串算出下一个数
s = '5'
s = chr(ord(s) + 1) # '6' 就得到了字符串的值
```

**字符串的方法。**
- 注意，那些序列的通用操作的表达式，和字符串特定的操作的表达式不同的。通用的操作，表达式就是那几种，而且对很多类型有效，但是字符串的特定操作，是str类的一个个方法，他们都用''.method()的格式，并且只对字符串有效。`str`类型的内置函数：
```python
>>>[i for i in dir(str) if not i.startswith('__')]
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
字符串修改：虽然字符串对象不可修改，但是变量可以重新赋值
```python
mystr = 'python'
mystr = 'awesome ' + mystr # 'awesome python' 字符串对象没有改变，而是变量重新赋值了
mystr = mystr[:] + ' 3.' + mystr[-1] # 'python 3.n' 加上切片索引，拼接也可以做到很多效果
s = mystr.replace('n', 'n 3.x') # 'python 3.x' 用replace方法也可以，而且更方便
# 如果操作非常频繁，可以转为list，需要的时候再拼接。或者使用 bytearray 字符串
L = list('python') # 打散为['p','y','t','h','o','n']
L[-1] = 'x'
s = ''.join(L) # 'pythox' 用''无缝拼起来
s = '-'.join(['2017', '4', '10']) # '2017-4-10' 拼接是用字符串将列表内元素的全连接起来
```
字符串解析：分析文本结构，并且提取固定信息的字符串。复杂的数据，还是用re模块比较好
- 如果是固定的结构，简单的字符串切片就可解决
```python
line = 'aaa bbb ccc'
col1, col2, col3 = line[:3], line[4:7], line[8:] # 'aaa'、'bbb'、'ccc'就筛出来了
```
- 如果是固定的分隔符，则最好使用split()方法
```python
line = 'aaa bbb ccc'
cols = line.split() # ['aaa','bbb','ccc'] 默认按照空白字符进行分割（空格、换行符\n，制表符\t），返回一个list
s = 'I am Python. Bye.'.split('.') # [' I am Python', ' Bye', '']
s = 'aaa'.split('a') # ['', '', '', ''] # 可以想象为：首尾各放一个引号，然后中间每个找到的字符都用两个引号替换。
```
其他常用的例子：
```python
mystr = 'awesome python'
mystr.upper() # 'AWESOME PYTHON' 全部转为大写。lower()全部转为小写。
mystr.capitalize() # 'Awesome python' 印刷格式。第一个单词的字母大写，其余小写。
mystr.replace('python', 'java') # 'awesome java' 替换
s = 'XXXpythonXXXpython'.replace('python','java',1) # 'XXXjavaXXXpython'出现多个，可以指定替换位置。不指定就全部替换
s = 'hello\n'.rstrip() # 清除每行的空白、换行符。这是最好的方式，会留下EOF
if 'py' in 'python': pass # 简单的成员测试也可以做到
where = 'XXXpythonXXXpython'.find('python') # 3 默认从前往后搜索，返回字符串出现的索引值，没有找到就返回-1
where = 'XXXpythonXXXpython'.find('python', 2, 12) # 3 用索引值指定搜索范围
mystr.index('o') # 4 字母o第一次出现的索引值。
mystr.count('o') # 2 字母o出现的次数
mystr.isalpha() # 是不是字母
mystr.startswith('p') # True 检测是不是以'p'开头。endswith()检测结尾
if mystr[:len('p')] == 'p':pass # 也可以用len和分片来检测开头。检测结尾：s[-len(sub):]==sub
mystr.ljust(20, '-') # 'awesome python------'，如果字符串不足20，就将'-'填充在末尾，直到达到20字符
mystr.ljust(20) # 'I am Python  ' 不指定填充字符，就用空格填充
```

**字符串格式化：**
- % 与 format：字符串格式化表达式%，基于C语言的printf模型。字符串格式化方法，则是Python2.6开始的。
%表达式：左侧是一个需要进行格式化的字符串，带有一个或者多个嵌入的转换目标；右侧在%后面放置一个或者多个对象（多个就要组成tuple）。
```python
s = 'my age is %s' % 20 # 任何对象都可以转成字符串，所以%s就可以。而字符串后面，一个字符，可以不用括号
s = 'that is %s %s bird' % (1, 'dead') # 多个字符串，必须用括号组成tuple
s = '%d %s %d = ?' % (1, '*', 5)
s = 'my age is %d' % 20 # 指定插入整数
In [8]: student = {'name': 'Windrivder', 'age': 21}
In [9]: "My name is {name}. I am {age}.".format_map(student)
Out[9]: 'My name is Windrivder. I am 21.'
```
格式化符号
|%s     |%r |%c|%d        |%i|u         |o  |x  |X|e         |E           |f
|--------|--------|
|任何对象|repr|字符|十进制整数|整数|无符号整数|oct|hex|HEX|科学计数法|大写的科学计数|小数
格式化表达式` %[(name)][flags][width][.precision]typecode`
```python
# %[(name)]typecode 用字典格式化字符串
'my age is %(n)d' %{'n':20} 
# %[flags]typecode 标志位可以指定左对齐、正负号、补零（6是数字宽度）
'__%d__%-6d__%06d__%+6d__' % (1234, 1234, 1234, 1234)  # __1234__1234  __001234__ +1234__
# %[width][.precision]typecode 打印长度（占多少格，没有补零就加空格）和数字精度（小数点后面留多少）
'__%3d__%5.2f__%06.2f__'%(1, 1.2345, 1.234567) # __  1__ 1.23__001.23__
# %e、%f、%g 用不同的方式表示浮点数
n = 1.23456789
'__%e__%f__%g__' % (n, n, n) # __1.234568e+00__1.234568__1.23457__
```
format()方法【待续】

**模式匹配 re 模块**
搜索／分割／替换，但因为它支持模式定义，所以更通用。

**编码**
Python3 编码问题：
1. ASCII 编码出现最早，只有大小写英文字母、数字和一些符号等 127 个字符，为了实现多语言表示，如中文的 GB2312 编码，日文的 Shift_JIS 编码等，Unicode 孕育而生，它将所有语言都统一到一套编码中；
2. 在 Python3 中所有字符串在内存中均是 Unicode 保存；
3. 当需要将文件保存到外设或进行网络传输时，就要进行编码转换，将字符转换为字节，以提高效率
```python
# encode 将字符转换为字节
>>> str = '优雅的Python'
>>> str.encode()			# 默认编码是 UTF-8
b'\xe4\xbc\x98\xe9\x9b\x85\xe7\x9a\x84Python'
>>> str.encode('gbk')
b'\xd3\xc5\xd1\xc5\xb5\xc4Python'
# decode 将字节转换为字符
>>> b'\xe4\xbc\x98\xe9\x9b\x85\xe7\x9a\x84Python'.decode()
'优雅的Python'
>>> b'\xd3\xc5\xd1\xc5\xb5\xc4Python'.decode('gbk')
'优雅的Python'
```
在 Python3 中，内存中的 Unicode 字符用 str 对象表示，对应于的，Python3 使用了一种全新的数据类型来表示字节，就是 bytes，所以 encode 转换后的字节流就不是 str 对象，而是 bytes 字节对象，它当然支持分片、索引、基本数值运算等操作，但 str 与 bytes 类型的数据不能进行`+`操作。
来看看 bytes 数据类型的定义：
```python
>>> byt = b'优雅的Python'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
>>> byt = b'Python'
>>> type(byt)
<class 'bytes'>
```
从上述例子中可以看出 bytes 对象不能由超出 ASCII 码范围的字符组成，只接受 ASCII 码这个范围的字符。
```python
>>> u'a'
'a'
>>> '\u0061'
'a'
>>> '中'.encode('unicode-escape')
b'\\u4e2d'
>>> b'@Aa'
b'@Aa'
>>> b'\x40\x41\x61'
b'@Aa'
>>> #-*- coding：utf-8 -*-
...
>>>
```

同样，从上面的例子我们还可以总结出一些坑爹的东西：
1. Unicode 码在 Python3 中有两种表示方式，`u'字符串'`和`\u四位十六进制数`；区分`r'字符串'` ，是表示不转义的原始字符串
2. 将字符直接以 Unicode 码保存使用`unicode-escape`
3. 在 Python 的交互式环境中，输出 bytes 对象时，可按 ASCII 码表示，或按十六进制`\x`表示
4. 在 Python 头声明`#-*- coding：utf-8 -*-`，是告诉 Python 编译器按`utf-8`的方式读取，这个声明并不能将 Python 文件保存本身保存成`utf-8`，这时候需要借助文本编辑器保存文件。


## 列表
列表是一个任意类型的对象的位置相关的有序集合。大小可变。最通用的序列。列表里保存的是其他对象的引用（而不是对象的拷贝），在Python解释器内部，列表是C语言指针数组。
列表和字符串不同：可以包含任何种类的对象（异构、任意嵌套）；可以原处修改（可变）。
因为可变性而产生的特有的序列操作：索引、分片的删除、修改；排序等等。
##### 列表的创建和常量表达
- ```python
a = [] # 空list。用list()也可以。
a = [1, 'a', 2, 3] # 4个不同类型的元素，组成一个list
a = ['a', ['b', 'c']] # 嵌套
a = list('some') # ['s', 'o', 'm', 'e']
a = list(range(4)) # [0, 1, 2, 3]
```

##### 序列操作
- **通用的序列操作**
```python
# 索引。读取一个值
a = [1, 2, 3]
a[0] # 1
a[-1] # 3
L = [['a', 'b', 'c'],
     ['d', 'e', 'f'],
     ['g', 'h', 'i']] # 嵌套构建矩阵
L[1][1] # 'e' 嵌套列表的索引
# 切片。得到一个新的列表
a[0:2] # [1, 2]
a[::-1] # [3, 2, 1] 复制，且翻转顺序
a[::2] # [1, 3] 步进切片
# 拼接和重复
b = [4, 5, 6]
a + b # [1, 2, 3, 4, 5, 6]
a * 2 # [1, 2, 3, 1, 2, 3]
# 迭代 和 in 成员测试
for item in a: pass
for key, value in enumerate(a): pass
if 1 in a: pass
# 长度、最大最小值、计数、索引运算
a = [1, 2, 3, 1]
len(a),min(a),max(a),a.count(1),a.index(1) # 4 1 3 2 0
```
- **序列的原处修改**
因为 list 是可变的，所以支持特有的序列的原处修改方法。虽然很强大，但还是extend、insert、append、pop之类的方法更常用。
```python
# del 切片 索引
a = [1, 2, 3]
del a[0] # [2,3] 索引删除
del a[0:2] # []切片删除
# 索引赋值。用新的对象引用，替换旧对象的引用
a = [1, 2, 3]
a[0] = 'x' # ['x', 2, 3]
a[3] = 'm' # 不能越界索引赋值。IndexError: list assignment index out of range
a[0] = ['m', 'n', 'p'] # [['m', 'n', 'p'], 2, 3]
a = [] # 空list 不能索引赋值
a[0] = [] # IndexError: list assignment index out of range
# 切片赋值。这个可就复杂了。相当于把那个片段删除，然后替换为等式右边的片段。这新旧两个片段长度可以不同，所以切片赋值，实际效果可以是 替换、增长、缩短
a = [1, 2, 3]
a[1:3] = ['y','z'] # [1, 'y', 'z'] 切片赋值，实现替换
a[1:4] = ['y'] # [1, 'y'] 切片赋值是可以越界访问的。实现缩短
a[1:2] = [] # [1] 如果把一个片段，替换为空片段，那就是删除。
a[1:3] = ['m', 'n', 'p'] # [1, 'm', 'n', 'p'] 切片赋值，实现增长
a = [] # 空list可以切片赋值，相当于extend()
a[:] =  [1, 2, 3] # [1, 2, 3]
```

##### 列表类的方法
```python
[i for i in dir(list) if not i.startswith('__')]
>>>['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
L = []
```
- 列表增减
```python
L = ['a', 'b', 'c']
L.append('d')  # ['a', 'b', 'c', 'd'] 在末尾添加一个对象，原地修改
print(L)
L = L + ['e'] # ['a', 'b', 'c', 'd', 'e'] 拼接也可以，但不是原地修改，而是新的list对象
print(L)
a = L.pop()  # ['a', 'b', 'c', 'd'] 默认取走末尾的对象
print(a)  # 'd'
a = L.pop(3)# ['a', 'b', 'c'] 取走 指定索引值的对象
print(L)
# pop和append结合，实现先进后出堆栈结构(last in first out/LIFO)，列表末端就是堆顶
L.extend(['x', 'y', 'z']) # ['a', 'b', 'c', 'x', 'y', 'z'] 拼接列表，但这是原地修改
L.insert(3,'M') #  ['a', 'b', 'c', 'M', 'x', 'y', 'z'] 指定索引位置上，插入一个值，其余的元素往后推
L.remove('M')  # ['a', 'b', 'c', 'x', 'y', 'z'] 删除一个指定值，没有返回值
L1 = L.copy() # 复制一个列表对象给L1
L.clear() # [] 删除列表内所有的元素
```
- 排序
```python
L = ['abc', 'ABD', 'aBe']
##### reverse()方法。简单地，将原来的顺序反转。没有返回值
L.reverse()  # ['aBe', 'ABD', 'abc']
##### reverse()内置函数。可以反转可迭代对象，生成一个可迭代的对象，而不是一个列表。
m = reversed(L) # <list_reverseiterator object at 0x0097A9D0>
re = list(m) # ['abc', 'ABD', 'aBe']
##### sort()方法。按照 ASCII 升序排列。请注意它没有返回值
L.sort()  # ['ABD', 'aBe', 'abc']
print(L)
L.sort(reverse=True)  # ['abc', 'aBe', 'ABD'] 关键字reverse将顺序反转
print(L)
L.sort(key=str.lower)  # ['abc', 'ABD', 'aBe'] 关键字key将每个元素用函数处理后，再进行排序
print(L)
# 如果函数返回多个值，先按第一个值排序，再按第二个值排序。如下 lambda x:(x < 0, abs(x))
lst = [1, -2, 10, -12, -4, -5, 9, 2]
lst.sort(key=lambda x:(x < 0, abs(x))) # [1, 2, 9, 10, -2, -4, -5, -12] 先按正负数排序，再按绝对值排序
# 列表内嵌字典，排序
data_list = [{'name': '1', 'v': '1.1'},
           {'name': '7', 'v': '1.2'},
           {'name': '5', 'v': '1.4'}]
data_list.sort(key=lambda item:(item['name'], item['v'])) # [{'name': '1', 'v': '1.1'}, {'name': '5', 'v': '1.4'}, {'name': '7', 'v': '1.2'}]
print(data_list)
# 列表内嵌列表、元组，也是类似
student_tuples = [('john', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'B', 10)]
student_tuples.sort(key=lambda t:(t[1],t[2])) # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
# 列表内的元素是自定义类的对象，按照某个属性排序。还是差不多的方式
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [Student('john', 'A', 15),
                   Student('jane', 'B', 12),
                   Student('dave', 'B', 10)]
student_objects.sort(key=lambda obj: (obj.grade,obj.age)) # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
##### sorted()方法，是对传入的对象进行迭代、排序，然后返回一个list。
lst = [1, -2, 10, -12, -4, -5, 9, 2]
stlist = sorted(lst,key=abs,reverse=True) # key和reverse的用法是一样的。但不是原处修改，而是返回list
print(stlist) # [-12, 10, 9, -5, -4, -2, 2, 1]
# 可用于任何可迭代对象，返回一个list。
L = sorted(x) # 对于不是list的对象，等价于：
L = list(x) # 先迭代生成一个list
L.sort() # 然后排序
L = sorted('Christ') # ['C', 'h', 'i', 'r', 's', 't'] 迭代字符串得到一个个字母，排序的列表
L = sorted({'name': '7', 'v': '1.2'}) # ['name', 'v'] 字典得到key、排序后的列表
```

##### 迭代和解析（更多请参见“迭代与解析”章节）
- ```python
a = [1, 2, 3]
b = [4, 5, 6]
num = sum(a) # 6
for x, y in zip(a, b): print(x,y) # zip()
for i,v in enumerate(a):print(i,v) # enumerate()
L = [i for i in range(10)] # 列表解析式
```




## 元组 tuple
元组，任意类型、任意嵌套。不可变的序列，除了这点，其余的特性与列表几乎相同。存储的依然是对象的引用。
Guido van Rossum说，元组用来收集简单的对象的容器，而列表是随时改变的数据结构。而且元组的不变性，提供了完整性，保证数据不会在共享引用等场景下被篡改，有点“常数”的意义。同时元组还可以用于列表不可用的地方，比如作为字典的key。所以，无需改变的地方，尽可能用tuple替代list。
- **创建（常量表达）**
```python
t = ()  # 空tuple，可以用tuple()创建
t = ('some',)  # 单个元素一定要有逗号，否则括号就是运算符，而整句是赋值
t = 'some',  # 没有括号也可以创建。但不建议这样做
t = (0, 'N', 1.2, 3)  # 多个不同的元素
t = 0, 'N', 1.2, 3  # 不用括号创建
t = tuple('some')  # ('s', 'o', 'm', 'e') 从可迭代对象创建
```
- 因为元组是不可变的，所以它只有序列的共有操作和方法。
```python
t = tuple('some')  # ('s', 'o', 'm', 'e')
# 索引、切片（切片返回新的tuple对象）
a = t[1]  # 'o'
b = t[1:3]  # <class 'tuple'>: ('o', 'm')
# 求长度
lenth = len(t)  # 4
# 合并、重复（返回新的tuple对象）
t2 = ('o', 'n', 'e')
T = t + t2  # ('s', 'o', 'm', 'e', 'o', 'n', 'e')
print(T)
T = t2 * 2  # ('o', 'n', 'e', 'o', 'n', 'e')
print(T)
# 迭代、in 成员测试
if 'o' in t: pass
for i in t: print(t)
L = [i for i in t]
# 通用运算
index = t.index('m')  # 2
count = t.count('o')  # 1
```
- 元组是不可变的对象，不提供任何修改的方法。如果需要“修改”，只能转为list，修改后转回tuple
```python
# 将元组排序，只能曲线救国
t = tuple('some')  # ('s', 'o', 'm', 'e')
temp = list(t) # ['s', 'o', 'm', 'e']
temp.sort()  # ['e', 'm', 'o', 's']
t = tuple(temp)  # ('e', 'm', 'o', 's')
# 用sorted()取代sort()
temp = sorted(t)
t = tuple(temp)  # 两步合一，一步到位 t = tuple(sorted(t))
```
- “可变的元组”——元组的不可变性仅仅针对元组顶层元素，而不是嵌套元素。嵌套的元素是可以修改的。
```python
t = ('a', {'b': 2}, [1, 2, 3, 4], 'd')
t[1].clear()  # 清空dict {'b': 2}
t[2].clear()  # 清空list [1, 2, 3, 4]
print(t)  # ('a', {}, [], 'd') 嵌套内容已经改变
```



## 字典
字典是一种映射，也是Python中唯一的映射。映射是一个其他对象的集合，通过键值对来存储对象。大小可变。字典也叫关联数组（Associative array）或散列表（Hash table）。字典里存储的也是对象的引用，而不是对象的拷贝。
字典和列表是Python中最常见、最常用、最灵活、最强大的数据类型。它们都可以包含任何种类的对象（异构、任意嵌套）、可以原处修改（可变）。只是list用位置索引，而dict用key索引。字典和列表一起，可以轻松地组建 json那样的复杂／高级数据结构。C／C++需要先设计／声明结构和数组，填写值，然后拼接，非常麻烦。
##### 字典的创建和常量表达
- 字典中的 key 不可变并且唯一，但 value 可变也可以重复。如果一个对象是可变的（比如列表list），那么它不可散列Unhashable，就不能作为集合set的元素，也不能作为字典dict的键。可以做key的类型：字符串、元组、数字
```python
# 直接从常量创建。适用于预置的数据，初始化赋值
d = {'food': 'apple', 'weight': 10, 'color': 'red'}
data = {'breakfast': {'apple': 2, 'egg': 1}, 'guest': ['Jhon', 'Anne'], 'time': '08:20'}  # 嵌套
print(d)
# 创建空dict，然后d[key]=value一项项赋值添加。适用于动态添加
d = {} # 创建空字典 等效dict()
d['food'] = 'apple' # 字典中还不存在这个key，所以是新增一个key:value
d['weight'], d['color'] = 10, 'red'
print(d)
# dict()构造函数，用关键字传参。适用于key都是字符串的情况
d = dict(food='apple', weight=10, color='red')  # 注意，key没有引号
print(d)
# dict()构造函数，从zip函数、元组列表创建。适用于从序列中创建字典
d = dict(zip(['food', 'weight', 'color'], ['apple', 10, 'red'])) # zip(keylist, valuelist)
d = dict([('food', 'apple'), ('weight', 10), ('color', 'red')]) # 就是list(zip(keylist, valuelist))的结果
# dict类的特殊方法创建
d = dict.fromkeys(['food', 'weight', 'color'])  # 不设置默认值，value就全部为 None
d = dict.fromkeys('some', 0)  # 不设置默认值0，value就全部为0
print(d)
# 解析式创建（仅用于Python3）
d = {i:ord(i) for i in 'some'} # {'e': 101, 's': 115, 'o': 111, 'm': 109}
d = dict((i, ord(i)) for i in 'some') # 字典解析式，本质是dict()和生成器的组合
gen = ((i, ord(i)) for i in 'some')
d = dict(gen)
d = {k:None for k in ['food','weight','color']} #模仿 dict.fromkeys(['food','weight','color'])
d = {k:0 for k in 'some'} # 模拟 dict.fromkeys('some', 0)
```

##### 字典操作
- **通用的操作（与list类似）**
```python
data = {'breakfast': {'apple': 2, 'egg': 1}, 'guest': ['Jhon', 'Anne'], 'time': '08:20'}
# 用key索引。嵌套的内容，就继续索引
time = data['time']  # '08:20'
apple = data['breakfast']['apple']  # 2
Anne = data['guest'][1]  # 'Anne'
# 重新赋值
data['time'] = '09:30' # 字典中已有这个key，所以是修改value
data['time'] += 'PM'
data['address'] = 'home' # 新增一个 key:value
del data['address'] # 删除一个 key:value
# len()
lenth = len(data) # 3 返回dict中key的个数
# in 和 for（最好别用has_key，Py3没有）
if 'time' in data: pass # dict中有没有这个key
for key in data:pass # 直接遍历字典，结果是遍历key
```
- **字典的操作**
避免missing key
```python
d = {'food': 'apple', 'weight': 10, 'color': 'red'}
name = d['name'] # KeyError: 'name' 索引不存在的key，越界访问引发异常
# 用get()方法。最简单
name = d.get('name') # None。没有默认值就返回None
name = d.get('name', 'Carol') # 'Carol' 有默认值就返回默认值‘Carol’
# 用 in 成员测试，结合if..else或者三元表达式
if 'name' in d:
    name = d['name']
else:
    name = 'Carol'
name = d['name'] if 'name' in d else 'Carol'
# name = (d['name'],'Carol') ['name' in d] 没法用。这是元组取值表达式，True是1，False是0
name = ('name' in d and [d['name']] or ['Carol'])[0] # 布尔运算，得到结果，然后从list中取值
name =  'name' in d  and d['name'] or 'Carol' # 这句是上句的缩写
# 用try语句捕获特定的KeyError也可以做到。但很捉急
try:
    name = d['name']
except KeyError:
    name = 'Carol'
```
copy、pop、update方法
```python
d = {'food': 'apple', 'weight': 10, 'color': 'red'}
# copy是完整复制
d2 = d.copy() # {'food': 'apple', 'color': 'red', 'weight': 10}
# pop是取走一个值。
color = d.pop('color')
print(color,d) # red {'food': 'apple', 'weight': 10}。如果key存在，取出value，删除key:value
# name = d.pop('name') # KeyError: 'name'。如果key不存在，且不设定默认值，将引发KeyError
name = d.pop('name', 'Carol') # name='Carol'。如果key不存在，就使用默认值
# update用新的dict对象覆盖旧dict
d3 = {'food': 'apple', 'weight': 10, 'color': 'red'}
d4 = {'food': 'pear','smell':'yummy'}
d3.update(d4) # 如果d3不存在key，用d4的合入；如果d3有，就用d4的覆盖。
print(d3) # {'weight': 10, 'color': 'red', 'food': 'pear', 'smell': 'yummy'}
```
遍历字典：直接遍历、keys/values/items方法遍历
```python
d = {'food': 'apple', 'weight': 10, 'color': 'red'}
# 简单地遍历字典，就是遍历key
for key in d: # food : apple | weight : 10 | color : red |
    print(key, ':', d[key], end=' | ')
# keys/values/items在Python2中得到相关的list，而在Python3则是可迭代的view对象
print(type(d.keys()), d.keys()) # <class 'dict_keys'>，dict_keys(['food', 'weight', 'color'])
key_list = list(d.keys()) # ['weight', 'color', 'food']。用list强制转成列表
for key in d.keys():
    print(key, ':', d[key], end=' | ')
for value in d.values():
    print(value,end=' | ') # 10 | red | apple |
print(d3)
for key, value in d.items(): # color : red | food : apple | weight : 10 |
    print(key, ':', value, end=' | ')
```
在Python2中，keys/values/items方法返回固化的list，而Python3中则是返回动态的dict view，可以动态地反应字典的修改。并且，keys和items返回的结果，可以像集合一样运算。
```python
# dict view 动态反应dict的修改（仅Python3）
d1 = {'food': 'apple', 'weight': 10, 'color': 'red'}
k_view = d1.keys()
print(list(k_view)) # ['weight', 'food', 'color']
del d1['food'] # 修改字典
print(list(k_view)) # ['color', 'weight'] 动态地反应了字典的改动
# keys和items方法的集合操作，values不支持（仅Python3）
d2 = {'color': 'red', 'a': 1, 'b': 2}
set1 = d1.keys() | d2.keys() # {'a', 'weight', 'color', 'b'} 并集Union
set1 = d1.keys() | {'x'} # {'weight', 'color', 'x'} 直接用集合与它进行并集运算
set1 = d1.keys() & d2.keys() # {'color'} 交集Intersection
set2 = d2.values() & d2.values() # TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
set3 = d1.items() & d2.items() # {('color', 'red')} 交集
set3 = d1.items() & {('color', 'red'), ('b', 2)} # {('color', 'red')} 直接用元组集合进行运算
```
对字典的key排序，再迭代
```python
# 方法一
ks = list(d.keys())  # python2直接用 ks = d.keys()
ks.sort()  # sort()没有返回值，千万不能 ks = ks.sort()
for key in ks:print(key,d[key])
# 方法二
ks = d.keys()
for key in sorted(ks):print(key,d[key])
# 方法三，最好的方法
for key in sorted(d):print(key,d[key])
```
字典大小比较
```python
# Python2
d1 = {'food': 'apple', 'weight': 10, 'color': 'red'}
d2 = {'food': 'pear', 'weight': 10, 'color': 'red'}
if d1 < d2: pass # True
if d1 == d2: pass # False
# Python3
d1 = {'food': 'apple', 'weight': 10, 'color': 'red'}
d2 = {'food': 'pear', 'weight': 10, 'color': 'red'}
# if d < d2: pass # unorderable types: dict() < dict()
if sorted(d1.items()) < sorted(d2.items()): pass  # True
if d1 == d2: pass # False
```
集合的常见的用途：
```python
# 1.构建数据。常用于接口和json
d = {"people": [
            {"firstName": "Brett", "lastName": "McLaughlin"},
            {"firstName": "Jason", "lastName": "Hunter"}
        ]
    }
# 2.用数字作key，假装是list
d = {0: 'p', 1: 'y', 2: 't', 3: 'h', 4: 'o', 5: 'n'}  # ['p', 'y', 't', 'h', 'o', 'n']
print(d[0])
# 3.如果不面向对象，字典是很好的记录数据的工具
people_1 = {'name': 'Jhon',
            'age': 22,
            'job': 'writer'}
# 4.实现稀疏数据结构。下例中，如果用list做成三维矩阵，那大部分都是空荡荡的
place = {(2, 3, 4): 88,
         (7, 8, 9): 99}
```
字典的存储是无序的，Python 中的 collections 提供`OrderedDict()`创建有序字典：
```python
from collections import OrderedDict
d = OrderedDict()
```




## 集合


集合（set）是一个无序不重复元素的集合。set和dict类似，也是一组key的集合，但不存储value。set的key，也是不可以放入可变对象（比如list），因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
因为set可以变化，所以不可散列（被固定引用），不能作为字典dictionary的key，也不能作为别的集合set的key。而另一种集合Frozenset是不可变的，可以作为字典和集合的key。
##### 集合的创建和常量表达
- 如果一个对象是可变的（比如列表list），那么它不可散列Unhashable，就不能作为集合set的元素，也不能作为字典dict的键。可以做key的类型：字符串、元组、数字。
```python
s = set()  # 创建空集合必须用 set()，因为{ }是空字典
fset = frozenset([1, 2, 4]) # Frozenset的创建与set相似，仅仅是调用的构造函数不同
s = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}  # {'Jack', 'Rose', 'Mary', 'Jim', 'Tom'} 重复元素在set中自动被过滤
# 用构造函数set()从各种可迭代对象中创建
s = set(['weight', 'food', 'color'])  # {'color', 'food', 'weight'}
s = set({'food': 'apple', 'weight': 10, 'color': 'red'})   # {'color', 'food', 'weight'}
s = set('some')  #  {'o', 'e', 's', 'm'}
# 集合解析式
s = set(i for i in 'some')  #  {'e', 'o', 's', 'm'} 集合解析式，生成器传入set()构造函数
s = {i for i in 'some'} # 集合解析式的语法糖
```

##### 集合操作
- Collection接口通用的操作
```python
# 迭代、in成员测试、len、max/min
s = set('some')
if 'o' in s:print(s)
for i in s:print(i)
lenth = len(s)  # 4
maxitem = max(s) # 's'
minitem = min(s)  # 'e'
```
- 集合类的方法
```python
>>>[i for i in dir(set) if not i.startswith('__')]
['add','clear','copy','difference','difference_update','discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>>[i for i in dir(frozenset) if not i.startswith('__')]
['copy','difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```
用集合进行数学运算，并、交、差等等。
```python
a = set('abcde')
b = set('defgh')
c = set('abcde')
d = set('cd')
print(a,b,c)           # {'r', 'b', 'a', 'c', 'd'}
# 判断
if not(a == b):print('not')  # 判断相等
if not a.isdisjoint(b): print('have intersection') # 判断两个集合不想交
if c <= a: print('sub1') # 判断c是不是a子集  等效a >= c
if c.issubset(a):print('sub2') # 判断c是不是a子集
if a.issuperset(c):pass # 判断c是不是a子集
if d < a: print('sub3') # 判断是不是真子集  等效 a > d
# 集合数学运算，返回一个新的集合
# 求2到N个集合的并集∪ 。一个主集，其他集合作参数。
E = a.union(b, c, d)  # {'d','g','b','e','f','a','c','h'} 等效表达式 a|b|c|d
print(E)
# 求2到N个集合的交集∩。一个主集，其他集合作参数。
E = a.intersection(b, c, d)  # {'d'} 等效表达式 a & b & c & d
print(E)
# 求一个集合与1到N个集合的差集 A-(B∪C∪D...) 。一个主集，其他集合作参数。
E = a.difference(b, d)  #{'b', 'a'} 等效表达式 a-b-d
# 求两个集合的去重，找出不同时存在的元素(A∪B)-(A∩B)
E = a.symmetric_difference(b) # {'g', 'b', 'a', 'h', 'c', 'f'} 等效表达式a ^ b 或者 (a|b)-(a&b)
E = a.copy()
s.add(4)  # 通过add(key)方法可以添加元素到set中，同一个元素可以重复添加，但不会有效果：{1, 2, 3, 4 }
s.remove(4)  #通过remove(key)方法可以删除元素： {1, 2, 3}
```
set类型特有的修改集合的操作，Frozenset不支持。
```python
a = set('abcde')
# 增加一个key
a.add('k') # {'k', 'e', 'a', 'd', 'c', 'b'}
# 删除一个key。如果这个key并不存在，就会报错
a.remove('k')  # {'a', 'd', 'e', 'c', 'b'}
# 删除一个key。如果这个key并不存在，那什么也不做
a.discard('j') # {'a', 'd', 'e', 'c', 'b'}
# 随机删除一个key，然后返回它
item = a.pop()
# 清空集合内的key
a.clear()
# 扩充集合 A = A∪B∪C...等效表达式 a = a|b|c 或者 a |= b|c
a, b = set('abcde'), set('defgh')
a.update(b, d)  # {'b', 'e', 'f', 'g', 'c', 'h', 'a', 'd'}
# 替换为交集 A = A∩B∩C...等效表达式 a = a & b & c 或 a &= b & c
a, b = set('abcde'), set('defgh')
a.intersection_update(b, d)  # {'d'}
# 替换为差集 A = A-(B∪C∪D...) 等效表达式 a = a-b-c 或 a -= b | c
a, b = set('abcde'), set('defgh')
a.difference_update(b, d)  # {'b', 'a'}
# 替换为两个集合去重后的集合。A = (A∪B)-(A∩B) 等效表达式 a = a ^ b 或 (a|b)-(a&b)
a, b = set('abcde'), set('defgh')
a.symmetric_difference_update(b)  # {'a', 'c', 'b', 'h', 'f', 'g'}
```














