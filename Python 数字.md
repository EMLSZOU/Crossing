# 定义

关于数值这种数据类型这里就不详细介绍概念了，列出了一些简单的例子：

```python
361, -361, 0, 66666		# 整型 --> int()
3.61, 3.14e-6, 0.0		# 浮点型 --> float()
3+6j, 3.0+6.0j, 6j		# 复数 --> complex([real[, imag]])
0b101010				# 二进制
0o177					# 八进制
0x9ff					# 十六进制
```

# 常见操作

下面是一些对数值进行操作的内建函数：

```python
In [1]: abs(10.)
Out[1]: 10.0

In [2]: abs(1.2-2.1j)
Out[2]: 2.418677324489565

In [3]: divmod(12, 21)	# 返回商和余数的元组
Out[3]: (0, 12)

In [4]: divmod(10, 3)
Out[4]: (3, 1)

In [5]: pow(2, 5)
Out[5]: 32

In [6]: pow(5, 2)
Out[6]: 25

In [7]: round(123.456, 2)	# 精确到小数点后指定位数
Out[7]: 123.46

In [8]: round(3.141592653, 3)
Out[8]: 3.142

In [9]: import math

In [10]: for eachNum in range(5):
    ...:     print(round(math.pi, eachNum))
    ...:
3.0
3.1
3.14
3.142
3.1416

In [11]: round(-3.1415)
Out[11]: -3
```

这里 **Python 核心编程**中给出的总结：

- 函数`int`直接截去小数部分（返回值为整型）
- 函数`math.floor`得到最接近原数但小于原数的整型（返回数字的下舍整数）
- 函数`round`得到最接近原数的整型（返回值为浮点型）

再来看看 Python 中的 random 模块常用的函数：

|       函数        |        功能         |
| :-------------: | :---------------: |
|   `choice()`    |  从一个序列中随机的抽取一个元素  |
|   `sample()`    |   提取出N个不同元素的样本    |
|   `shuffle()`   |    打乱序列中元素的顺序     |
|   `randint()`   |      生成随机整数       |
|  `randrange()`  | 指定基数递增的集合中获取一个随机数 |
|   `random()`    | 生成0到1范围内均匀分布的浮点数  |
| `getrandbits()` |   N位随机位(二进制)的整数   |
|    `seed()`     |      修改初始化种子      |

```Python
In [1]: import random
In [2]: L = [1, 2, 3, 4, 5, 6]
In [3]: random.choice(L)
Out[3]: 6

In [4]: random.choice(L)
Out[4]: 2
In [5]: random.choice(L)
Out[5]: 5
In [6]: random.sample(L, 2)
Out[6]: [5, 6]
In [7]: random.sample(L, 3)
Out[7]: [5, 1, 3]
In [8]: random.shuffle(L)
In [9]: L
Out[9]: [6, 5, 2, 1, 4, 3]
In [10]: random.randint(0, 100)
Out[10]: 90
In [11]: random.randint(0, 100)
Out[11]: 42
In [12]: random.randrange(10, 100, 2)
Out[12]: 60
In [13]: random.randrange(10, 100, 2)
Out[13]: 80
In [14]: random.random()
Out[14]: 0.33979450941843936
In [15]: random.random()
Out[15]: 0.27086856702599793
In [16]: random.getrandbits(101)
Out[16]: 1221044021633007371540182353021
In [17]: random.getrandbits(200)
Out[17]: 1317656193513780304331528523139074202611968854868963255105569
In [18]: random.seed(123456)
```


## 数字
数字类型，是一组类似数据类型的归类。包括：整数int、浮点数float、复数complex、固定精度浮点数Decimal、分数Fraction、集合Set、布尔型bool。
数字的内置工具还包括：数学函数、数学模块
builtin的数字类型：整数int、浮点数float、布尔值bool、复数complex
**整数**包括正负，并且有无穷的精度（意思是不管多大，都不会超出内存限额）。
在Python2.x中，如果一个整数超过内存限制，会自动转成 long int，数字后面加个L。但是Python3.x中，只有int，无穷精度。
```python
>>> 0b1 # 二进制bin，以数字0字母b开始
1
>>> 0o001 # 八进制oct，以数字0字母o开始
1
>>> 0x01 # 十六进制hex，以数字0字母x开始
1
```

**浮点数 float**
`1.0   2.3   3.14e-10`
算术中，只要出现浮点数float，就自动将相关的数据转成浮点数的精度和运算法则（相当于C语言的double）
```python
a = 1.0 + 5  #  6.0
b = 1 + 5   #  6
```
**复数complex**
复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

hex()、oct()、bin() 把一个十进制数值转成相应进制的字符串，而 int(str, base)则把字符串按指定的进制，转成十进制整数。

**数学运算**
```python
>>> 5 + 4  # 加法
>>> 4.3 - 2 # 减法
>>> 3 * 7  # 乘法
>>> 2 / 4  # 除法，得到一个浮点数。数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。并且在混合计算时，Python会把整型转换成为浮点数。（具体见运算）
>>> 2 // 4 # 除法，得到一个整数
>>> 17 % 3 # 取余
>>> 2 ** 5 # 乘方
% 取模运算
如果整数int 与 浮点数float 混合运算，整数就会自动转化为float
a = 17/3   # 5 地板除。两个int相除，返回int。
b = 17/3.0  # 5.66... 真除法。一旦出现float，就int转成float，整个运算执行float法则
c = 17//3.0  # 5.0  强制地板除。即使出现浮点数，按照float法则运算，但强制截尾
```

**类型转换**
	`向上转型，自动转换：int<float<complex`
不可以在数字类型和其他类型之间使用自动转换，比如 a = ‘some’+ 10
	`向下转型，强制转换，将会截尾：int(3.1415) 为 3`
运算符重载
某些操作符能够根据所处理的内置对象的类型，而执行不同的操作。比如
```python
a = 10 + 5  # 数字型，执行加法
a = ‘some’+ ‘body’ # 对于 str 或者 list，执行合并
```
显示格式
```python
    num = 1/3
    r_num = repr(num)  # 源数据显示模式，可以显示额外的细节
	str_num = str(num)  # 用户友好显示模式
	# 两个函数都可以把任意对象转换成字符串，但是效果不太相同。
    print(r_num,'\n',str_num)
```

**小数、十进制数（固定精度浮点数）Decimal**
Decimal提供了固定小数位的浮点数（所谓固定精度），还可以定义舍入的方式（比如四舍五入）。
- 两种方式创建：整数int，字符串str
```python
    import decimal
	a = decimal.Decimal(1)/decimal.Decimal(10)
    from decimal import Decimal
    a = Decimal('0.1')
```
- 创建时可以设置小数运算的精度
```python
    import decimal
    a = decimal.Decimal(1) / decimal.Decimal(7)
    print(a) #不设精度，无限循环小数0.1428571428571428571428571429
    decimal.getcontext().prec = 2  # 设定精度
    b = decimal.Decimal(1) / decimal.Decimal(7)
	print(b)  # 0.14 固定位数小数
```
- 还可以用with 环境管理器设置精度
```python
	import decimal
	    with decimal.localcontext() as context:
	        context.prec = 2
	        b = decimal.Decimal(1) / decimal.Decimal(7)
	    print(b)   # 0.14
	    a = decimal.Decimal(1) / decimal.Decimal(7)
	    print(a) #离开with，精度还原 0.1428571428571428571428571429
```

**分数 Fraction**
- 创建
```python
	from  fractions import Fraction
	x = Fraction(1,3)  # 2个整数，创建分数
	y = Fraction(4,6)
	m = Fraction('1.25')  # 用一个字符串、里面是浮点数，创建分数 5/4
```
接下来，可以像普通的数字一样使用分数 x+y, x-y, x/y, x*y, x**y  `**  乘方`
分数与小数，二者是近亲。浮点数因为内存空间有限，所以精度有限，而分数和小数能提供更准确、更直观的结果。
- 更准确：
```python
    from decimal import Decimal; from fractions import Fraction
    a_float = 0.1 + 0.1 + 0.1 - 0.3  # 本应为 0，却不为0，因为float的精度不够
    a_decimal = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')  # 结果 0.0
	a_fraction = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)  # 结果 0
```
- 更直观：分数，是小学生的知识，简单易懂；而固定位数的小数 0.33，也比 杂乱的浮点数 0.33333333 更易读
```python
import decimal
    from fractions import Fraction
    with decimal.localcontext() as context:
        context.prec = 2
        a_float = 1/3 # 0.3333333333333333
        a_decimal = decimal.Decimal(1)/decimal.Decimal(3)  # 0.33
        a_fraction = Fraction(1, 3) # 1/3
```

**布尔值 bool**
调用`bool()`可以检查变量的真假值`True`或`False`。
在Python2中是没有布尔型的，它用数字0表示False，用1表示True。到Python3中，把True和False定义成关键字了，但它们的值还是1和0，它们可以和数字相加。


**等值 与 同一：**
- 操作符`==`测试两个对象的数值是不是相等。操作符`is`测试两个是不是同一个对象（内存地址、id）。
- 但是有时候，虽然逻辑上不是同一个对象，is 运算却得到了True。这是因为Python把数字、小字符串都缓存了，然后让各个变量共享了。
```python
a, b = 1, 1
print(a is b, a == b)  # True True
c, d = 'you', 'you'
print(c is d, c == d)  # True True
```

**数据结构，递归比较大小：**
- 数字类型，通过大小进行比较。
- 字符串按照ASCII顺序、一个一个字符地比较。列表和元组，从左到右对每部分的内容进行比较。
- 字典通过排序后进行比较，Python2会自动排序比较，而Python3比较大小的时候则需要 sorted(d1)>sorted(d2)先排序后比较。
```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

**连续布尔值运算：**
- ```python
x,y,z = 2,4,6
if x<y<z: pass  # 相当于 x<y and y<z
if x<y>z:pass  # 相当于 x<y and y>z
if x==y<z:pass  # 相当于 x==y and y<z
```

**布尔运算 bool(obj) 的规则：**
- 基本类型（每个类型都存在一个值会被判定为False）：
|  类型  | False             | True                               |
| :--: | :---------------- | :--------------------------------- |
|  布尔  | False （与0等价）      | True （与1等价）                        |
| 字符串  | ""（ 空字符串）         | 非空字符串，例如 " ", "blog"               |
|  数值  | 0, 0.0            | 非0的数值，例如：1, 0.1, -1, 2             |
|  容器  | [], (), {}, set() | 至少有一个元素的容器对象，例如：[0], (None,), [''] |
| None | None              | 非None对象                            |
- 自定义类型：
    - 如果定义了__nonzero__()方法，会调用这个方法，并按照返回值判断这个对象等价于True还是False
    - 如果没有定义__nonzero__方法但定义了__len__方法，会调用__len__方法，当返回0时为False，否则为True（这样就跟内置类型为空时对应False相同了）
    - 如果都没有定义，所有的对象都是True，只有None对应False
- 如果你要判断一个对象是不是为 False，建议最好别这样
```Python
if a == '':pass  # 判断是不是空的数据
if a == '' or a == None: pass  # 判断是不是空的数据，或者是None
```
而应该这样：
```python
if a: pass
if not a: pass
```
执行中会调用`__nonzero__()`来判断自身对象是否为空并返回`0/1`或`True/False`，如果没有定义该方法，Python 将调用`__len__()`进行判断，返回`0`表示为空。如果一个类既没有定义`__len__()`又没有定义`__nonzero__()`，该类实例用 if 判断为`True`。
P152


**占位符 None**
- 空值是Python里一个特殊的值，用None表示。None对象是一个特殊的Python对象，它总是False，一般用于占位。它有一块内存，是一个真正的对象。它不代表未定义，事实上它有定义。None是所有函数和方法的默认返回值。
- None不是False：False和True对应，它作为布尔类型用来描述逻辑中“假”这个概念；None和“存在元素”相对应，“存在元素”反过来为“不存在元素”，也就是None。
None和java的null是不同的，null是空字符，而Python的None是NoneType类的一个实例，很像C语言的NULL指针。
```python
>>> type(None)
<class 'NoneType'>
```

**内置的数学函数和模块**，有很多的数学特有操作：
- 内置数学函数：pow、abs、round、int、hex、bin
- 内置数学模块：random、math
```python
    pow(2, 4)  # 等价于 2**4 = 16
    abs(-42)  # 绝对值运算，|-42| = 42
    sum([1, 2, 3, 4])  # 求和运算 1+2+3+4 = 10
    min([1, 2, 3, 4])  # 求最小值，结果为1。max()求最大值
    import math
    p = math.pi  # 3.141592653589793
    s = math.sqrt(144)  # 求平方根方式 1 ，结果为 12.0
    s = 144 ** 0.5  # 求平方根方式 2
	s = pow(144, 0.5)  # 求平方根方式 3
    import random
    random.random()  # 产生一个随机的浮点数，比如 0.9139864997839369
    random.randint(1, 10)  # 产生一个1-10之间的随机整数
    random.choice(['a', 'b', 'c'])  # 随机选择
```

**其他数字扩展：**
Numpy（Numeric Python）是第三方模块，被称为 免费易用的Matlab。支持矩阵、向量、高级计算。
Scipy
