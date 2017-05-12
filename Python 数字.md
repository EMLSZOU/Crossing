

## 数字
数字类型，是一组类似数据类型的归类。包括：整数int、浮点数float、复数complex、固定精度浮点数Decimal、分数Fraction、集合Set、布尔型bool。
数字的内置工具还包括：数学函数、数学模块
**整数int**
整数包括正负，并且有无穷的精度（意思是不管多大，都不会超出内存限额）。
在Python2.x中，如果一个整数超过内存限制，会自动转成 long int，数字后面加个L。但是Python3.x中，只有int，无穷精度。
数字常量表示方式：二进制八进制十进制十六进制 p134、p118
**浮点数 float**
`1.0   2.3   3.14e-10`
算术中，只要出现浮点数float，就自动将相关的数据转成浮点数的精度和运算法则（相当于C语言的double）
```python
a = 1.0 + 5  #  6.0
b = 1 + 5   #  6
```
hex()、oct()、bin() 把一个十进制数值转成相应进制的字符串，而 int(str, base)则把字符串按指定的进制，转成十进制整数。

**数学运算**
p120 Python 表达式操作符

- 除法的规则
```python
print(10/5)   # 结果为  2.0  除法永远返回 float
print(7//3)   # 2   整除（地板除 floor division）
print(7//-3)  # -3
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

**二进制运算**
二进制，位操作 p136
移位
或运算
与运算

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

**集合 set**
- 一些唯一的、不可变的对象的一个无序集合/Collection。支持一般的数学集合操作。广泛应用于数学和数据库工作中。
集合set既不是序列，也不是映射。集合很像一个只有key没有value的字典：可迭代、可增减、能包含各种类型的对象。
支持len()，可迭代。但不能序列操作——索引和切片。
P146集合操作的各种方法
```python
s1 = set()   # 创建空集合。dict = {} 这是创建空字典
x = set('abcde')  # 传入一个可迭代对象，构造函数自动创建一个set，结果{'a','b','c','d','e'}
a_dict = {'d': 1, 'e': 2, 'x': 3, 'y': 2, 'z': 3}
y = set(a_dict)  # 字典的key构建了set ，结果{'e', 'd', 'x', 'y', 'z'}
print('e' in x)  # 布尔运算：成员测试，'e'是集合x的成员吗？
print(x|y)  # 数学求并集 {'a', 'b', 'c', 'd', 'e', 'x', 'y', 'z'}
print(x&y)  # 交集 {'d', 'e'}
print(sorted(x^y))  # 并集，然后减去交集。也就是 两个集合不重合的部分 {'a', 'b', 'c', 'x', 'y', 'z'}
print(x>y)  # 布尔运算，子集测试，y是x的子集吗？
```

**布尔值 bool**
进行逻辑判断（比如if）时，布尔运算规则。
- 基本类型（每个类型都存在一个值会被判定为False）：
    - 布尔型，False表示False，其他为True
    - 整数和浮点数，0表示False，其他为True
    - 字符串和类字符串类型（包括bytes和unicode），空字符串表示False，其他为True
    - 序列类型（包括tuple，list，dict，set等），空表示False，非空表示True
    - None永远表示False
- 自定义类型：
    - 如果定义了__nonzero__()方法，会调用这个方法，并按照返回值判断这个对象等价于True还是False
    - 如果没有定义__nonzero__方法但定义了__len__方法，会调用__len__方法，当返回0时为False，否则为True（这样就跟内置类型为空时对应False相同了）
    - 如果都没有定义，所有的对象都是True，只有None对应False
- 连续布尔值运算：
```python
    x,y,z = 2,4,6
    if x<y<z: pass  # 相当于 x<y and y<z 
    if x<y>z:pass  # 相当于 x<y and y>z
    if x==y<z:pass  # 相当于 x==y and y<z
```
P152


**占位符 None**
- 空值是Python里一个特殊的值，用None表示。None对象是一个特殊的Python对象，它总是False，一般用于占位。它有一块内存，是一个真正的对象。它不代表未定义，事实上它有定义。None是所有函数和方法的默认返回值。
- None不是False：False和True对应，它作为布尔类型用来描述逻辑中“假”这个概念；None和“存在元素”相对应，“存在元素”反过来为“不存在元素”，也就是None。
None和java的null是不同的，null是空字符，而Python的None是NoneType类的一个实例。
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
