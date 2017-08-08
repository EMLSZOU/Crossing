
# 执行Python程序
3种方式运行Python程序：交互执行、解释模式执行代码、解释模式执行文件。
### 交互执行：
- Windows的CMD，或者 Linux/Unix的Shell里，输入Python回车，调出Python解释器，然后一行行输入代码。
```python
	>>> if 0 < 3:       # 主提示符
	...     print "Some"  #从属提示符，表示缩进。复合语句之后的代码组（子句）
	...     # 从属提示符，表示下面的是输出
	Some
```
- 每次运行一个程序单元（语句或一个语句块），由空行结束代码块。
```python
	>>> a = []
	>>> for char in "about":
	...     a.append(char) # 两次回车。第一次是换行，第二次是输入一个空行，结束for代码块。
	...
	>>> a   # 有时候，不需要刻意写 print 语句
	['a', 'b', 'o', 'u', 't']
```
- 主要用于实验，快速地弄懂一段代码究竟是什么作用。也可以用来快速测试组件或者模块
```python
	>>> import os
	>>> os.getcwd()
	'D:\\PyProject\\CloudInfraDeploy\\glue\\Src\\glue'
	>>> dir(os)  # 查看所有变量、模块、函数等等
	['F_OK', 'O_APPEND', ……]
	>>> help(os) # 查看帮助文档
	Help on module os:……
```
### 解释模式执行文件
最常用。其实IDE里也是这样运行Python的。
    1. 程序员写好源代码  demo.py 文件
    2. Python将源代码编译（本质是翻译）成字节码  demo.pyc文件。这不是build/make，字节码不是二进制文件（CPU指令），所以是平台无关的。并且，如果已经有 demo.pyc，而且源代码没有改变过，那就不会再次生成 pyc 。如果不能写入硬盘，pyc就会放在内存，运行后删除。.pyc文件也是发布Python程序的方法之一。此时并不需要提供.py源代码。
    3. Python虚拟机/PVM，是代码与计算机硬件之间的软件逻辑层。载入 demo.pyc ，在PVM内部编译、运行 pyc文件。实际上PVM不是一个独立的程序，它只是迭代运行字节码指令的一个大循环而已，它是Python系统的一部分。

CMD>Python  demo.py   --运行命令的格式（Unix的Shell也一样）
CMD>Python  demo.py > log.txt  --将输出重定向
CMD>C:\Python35\python  D:demo.py   --Python解释器和脚本都可以**使用绝对路径**。
所以，Python的开发和编译、执行，都在同一个系统内进行的。完全不需要编译，大大缩短开发时间。
顶层入口源代码文件，一般叫脚本，可以不以 .py结尾；而被导入的文件，一般叫做模块，强制使用 .py结尾。
**直接运行代码**
 Linux/Unix里，编写一个Python文件，然后双击运行。 很少见，很少用，这也是`#!/usr/bin/env python`存在的理由。
写好Demo 文件（无.py后缀），内容如下：
```python
	#!/usr/bin/env python
	# -*- coding:utf-8 -*-
	print("HelloWorld")
```
改变模式  ` chmod r+x Demo`
直接运行    ` ./Demo`

### Python的其他实现方式
• Psyco/PyPy：在运行时，将部分字节码转成二进制指令，速度提高4倍以上。PyPy是后起之秀。.pyc加载更快，运行无差别；.pyo，优化后的文件，运行更快。这些都是通过源代码编译字节码，然后在虚拟机运行。
• CPython，就是上面的过程。官方标准，C语言编写，速度快，最完整健全。
• Jython，为了与Java集成而产生。可以让py文件转化为Java字节码，然后就像一个Java程序一样在JVM中执行。
• IronPython，为了与.Net/C#平台集成。
• Shedskin C++：将Python代码转成C++字节码，然后编译链接。
• 转为可执行程序：冻结二进制文件 Frozen Binary，将字节码、PVM、支持文件捆绑为一个软件包。Windows 用 py2exe 做成 exe文件，Unix/Linux 用 PyInstaller转成二进制文件。

运行速度：ShedSkin>PyPy>IronPython>Cpython 2>C Python3>Jython

