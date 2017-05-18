##文件 file
调用内置函数open会创建一个文件对象，而后就可以用这个对象的方法来读写计算机上的文件。
文件对象和其他类型的对象很不相同，无法通过常量语法（比如 l = [1,2,3] ）创建。
##### 文件对象的创建
f = open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
- file参数，用字符串指定文件的存放位置。Windows默认格式是\，Linux是/，Python无所谓，但要防止转义。如果文件不存在，会抛出一个IOError的错误，FileNotFoundError: [Errno 2] No such file or directory。
```python
# 没有路径，文件在当前目录
file = open('t.txt')
# 相对路径
file = open(r'./t.txt')  # 当前目录
file = open(r'../f.txt') # 上一级目录下的文件
# 绝对路径
file = open('D:\\GitbackUp\\nf.txt')  # 防止转义，特别是出现合法转义组合
file = open(r'D:\GitbackUp/f.txt')  # 用r避免转义的烦恼。/和\混用也可以
```
- mode参数，用字符串指定文件的打开模式，也就是如何使用该文件。
'r' read表示只是读取文件；
'x' create表示新建文件并且写入文件，如果文件存在，FileExistsError: [Errno 17] File exists。连'x+'都是如此。
'w' write表示只是写入文件（如果存在的同名文件将被覆盖），不可以读取文件数据；
'a' append表示写入的内容追加到文件末尾（不覆盖原有的数据），不可以读取文件数据。
'+' 表示以更新模式打开文件，'r+'模式可写入，而'w+'和'a+'虽然read()不会报错，但是读不到数据。
'b' 表示以二级制模式打开。与默认值't'对应
't' 表示以文本模式打开。
默认值是rt，所以通常文件以 文本 打开，这意味着，你从文件读出和向文件写入的字符串会被特定的编码方式（要么是系统默认的UTF-8格式，要么是指定的格式）编码。模式后面的 'b' 以 二进制模式 打开文件：数据会以字节对象的形式读出和写入，这种模式应该用于所有不包含文本的文件。
在文本模式下，读取时默认会将平台有关的行结束符（Unix上是 \n , Windows上是 \r\n）转换为 \n。在文本模式下写入时，默认会将出现的 \n 转换成平台有关的行结束符。这种暗地里的修改对 ASCII 文本文件没有问题，但会损坏 JPEG 或 EXE 这样的二进制文件中的数据。使用二进制模式读写此类文件时要特别小心。
'U' 表示开启universal newline mode (deprecated)写入。U模式不赞成使用。对于Python3没有任何作用，以后可能会删除这个功能。
常用的有
```python
# 默认值
file = open(r'D:/GitbackUp/f.txt',mode='rt')
# 读取和写入，并且追加到文件末尾而不覆盖
file = open(r'D:/GitbackUp/f.txt',mode='r+')
# 覆盖写入（虽然不引发Error，但read()无效）。
file = open(r'D:/GitbackUp/f.txt', mode='w+')
# 追加写入（虽然不引发Error，但read()无效），追加到文件末尾而不覆盖
file = open(r'D:/GitbackUp/f.txt',mode='a+')
# 读取二进制文件
file = open(r'D:/GitbackUp/f.bin',mode='rb')
```
- buffering参数，控制写入文件时的缓冲大小，0就是不缓存，调用write()时立即写入。但设置为0是违法的。

##### 文件对象的使用
- 文本读取：最好是不调用任何read方法，而是在迭代环境中自动读取。
- 文件关闭：如果文件对象不再被使用了，文件对象会被自动清理，而文件也会被自动关闭。然而，最好还是要有关闭的动作，要么是手动的 f.close() 关闭调用，要么是 with...as...环境管理器的自动关闭。
```python
#在Python3 中，文本与二进制的文件对象是截然不同的。
f = open('data.txt')  # 文本文件，内容解析成字符串，默认执行Unicode编码
f = open('data.bin','rb')  # 二进制文件，解析二进制
#读取操作
f = open('data.txt')  # 处理模式默认值为 'r'
text = f.read()  # 读取文件内所有的内容，返回字符串对象，
text = f.read(5) # 读取文件内指定的字节数
linestr = f.readline()  # 读取下一行，返回字符串(包括换行符)
linelist = f.readlines()  # 读取文件所有的内容，返回list，每一行就是一个元素（包括换行符）
linelist = list(f) # 等效 f.readlines()
print(text)  # 将内容打印
f.close()  # 关闭文件
text.split()  # 内容可以继续进行处理
# 在迭代环境自动读取，是最好的文件读取方式
for line in f: pass
```
- 文件读写：一般情况下，文件读写的内容都是字符串，所以非字符串对象必须转为字符串才能写入，而字符串要经过 int()、eval()之类的才能转为其他对象。如果要进行特殊的对象读写，struct模块处理二进制，pickle模块进行对象持久化。
```python
#写入操作
file = open(r'D:/GitbackUp/f.txt', mode='w')
char_num = file.write('明月几时有\n把酒问青天\n')  # 必须自己手动加入\n
print(char_num)  # 11 在Python3中，会返回写入的字符数
file.writelines(['不知天上宫阙\n', '今夕是何年\n'])  #  传入的参数是 collections.Iterable[unicode]
file.flush()  # 强制清空缓冲，写入磁盘
file.close()  # 关闭文件也可以强制写入磁盘
# 用with...as...环境管理器
with open(r'D:/GitbackUp/f.txt', mode='w') as file:
    char_num = file.write('明月几时有\n把酒问青天\n')
    print(char_num)
    file.writelines(['不知天上宫阙\n', '今夕是何年\n'])
# 用try...finally...手写环境管理器
try:
    file = open(r'D:/GitbackUp/f.txt', mode='w')
    char_num = file.write('明月几时有\n把酒问青天\n')
    print(char_num)
    file.writelines(['不知天上宫阙\n', '今夕是何年\n'])
    file.flush()
finally:
    file.close()
```
- 文件指针和查找：文件对象是在字节偏移的基础上访问的。
f.tell() 返回一个整数，代表文件对象在文件中的指针位置，该数值计量了自文件开头到指针处的比特数。
f.seek()方法可以改变文件对象指针，到指定的地方进行读写。f.seek(offset, index)。指针在该操作中从指定的引用位置 index 移动 offset 比特。 index=0 表示自文件起始处开始（默认参数，可以省略），1 表示自当前文件指针位置开始，2 表示自文件末尾开始，默认值为零。在文本文件中（没有以 b 模式打开），只允许从文件头开始寻找（有个例外是用 seek(0, 2) 寻找文件的最末尾处）而且合法的 index 值只能是 f.tell() 返回的值或者是零。其它任何 index 值都会产生未定义的行为（因为文本的每个字节有特定的长度）。
```python
with open('data.pkl', 'rb') as file:
    print(file.read(10))  # b'\x80\x03}q\x00(X\x01\x00\x00'
    print(file.tell())  # 10
    file.seek(-5, 1)  # 在当前位置，往回走5字节
    print(file.read(5))  # b'(X\x01\x00\x00'
    print(file.tell())  # 10
    file.seek(10, 1)  # 在当前位置，往下走10字节
    print(file.read(5))  # b'trq\x02X'
    file.seek(0)  # 回到文件起始处
```

- 文件缓冲：默认情况下，输出文件总是缓冲的，也就是说write等方法写入的数据不会立即从内存写到硬盘的文件中。关闭文件、f.flush()就可以迫使缓冲数据写入磁盘文件。如果open()创建文件对象时，buffering=0，就不缓冲而是立即写入，但是这会影响系统性能，所以是不允许的。

##### 二进制读写
- Python3默认所有的字符串都是utf-8，所以用str.encode和decode就可以做到字符串到二进制的转换
```python
# 以二进制写入字符串
file = open(r'D:/GitbackUp/a.bin', mode='wb')
string = '明月几时有\n把酒问青天\n'
bin_data = string.encode()  # 所有的字符串，经过编码成二进制数据
file.write(bin_data)  # 写入文件
bin_list = [str.encode(i) for i in ['不知天上宫阙\n', '今夕是何年\n']]
file.writelines(bin_list)  # 写入二进制组成的列表
file.close()
# 读取二进制数据，然后解码为字符串
file = open(r'D:/GitbackUp/a.bin', mode='rb')
bin_data = file.read()  # b'\xe6\...\n' 读取得到二进制数据
string = bin_data.decode()  # 明月几时有...就正确解析出字符串
```
- 如果要二进制读写复杂的数据，就需要 struct 模块。
**`struct.pack(fmt, *args)`**
args 是写入的1到N个数据，必须与fmt向对应
fmt 指定写入的数据的格式，比如，i代表一个int，ii为2个int，i5sf为1个int5个字符的字符串1个小数。各种fmt代码请查阅doc
```python
# 写入数字
import struct
with open(r'D:/GitbackUp/a.bin', mode='wb') as file:
    int_num = 10
    bin_data = struct.pack('i', int_num)  # b'\n\x00\x00\x00' 转成二进制数据
    char_num = file.write(bin_data)  # 写入了4个字符
with open(r'D:/GitbackUp/a.bin', mode='rb') as file:
    bin_data = file.read()  # b'\n\x00\x00\x00' 读出二进制数据
    int_num,= struct.unpack('i', bin_data)  # 10。注意返回的是元组，等式左边要有逗号
# 写入混合类型的数据
with open(r'D:/GitbackUp/a.bin', mode='wb') as file:
    int_num = 10
    float_num = 1.234
    string = '明月几时有\n'
    bin_str = str.encode(string)  # 字符串必须转成二进制，并且指定长度，才能pack
    bin_data = struct.pack('i%dsf' % len(bin_str), int_num, bin_str, float_num)  # 打包二进制数据
    char_num = file.write(bin_data)  # 写入了24 个字符
with open(r'D:/GitbackUp/a.bin', mode='rb') as file:
    bin_data = file.read()  # 读出二进制数据
    int_num, bin_str, float_num = struct.unpack('i%dsf' % len(bin_str), bin_data)  # 字符串必须指定长度才能unpack
    string = bin_str.decode()  # 二进制数据的字符串，还必须解码
```

##### Python对象的读写
- 如果是Python的内置数据类型，可以将数据转化为字符串，然后存储到磁盘，读取的字符串，转化为Python内置对象。int、float、eval能将字符串转为Python对象。然而，eval()会执行任何字符串表达式，甚至是…攻击性的恶意代码，这时候就不是eval而是devil。用ast模块可以缓解一下。
```python
tuple_data = (1, 'a', False, {'a': 1, 'b': 2})
# 如果是 tuple，则没法用 格式化语句。必须用str(tuple_data)
s = '%s' % (tuple_data) # TypeError: not all arguments converted during string formatting
s = str(tuple_data)
import ast
a = ast.literal_eval('{"key1":"value1", "key2":"value2", "key3":"value3"}')
```
- 如果是内置对象构成的复杂数据结构，无论转成字符串还是从字符串转为内置对象，都非常困难。用 **json模块** 就可以序列化Serialization、存储。
```python
import json
# json.dumps()序列化：将json数据结构转为字符串，"dump to str"。字符串可以写入到文件
data_str = json.dumps([1, 1.2, 'str', True, {'a': 1}, None])  # 列表
print(data_str, type(data_str))  # [1, 1.2, "str", true, {"a": 1}, null] <class 'str'>
data_str = json.dumps({'a': 1, 'b': 0.2, 'c': 'str', 'd': [1, 'm'], 'e': None, 'f': False})  # 字典
print(data_str, type(data_str))#{"a": 1, "d": [1, "m"], "b": 0.2, "c": "str", "e": null, "f": false} <class 'str'>
# json.loads()反序列化：将字符串转为json数据结构，"load from str"。字符串可以从文件读取
data = json.loads(data_str)
print(data, type(data))
```
如果将dumps()-->写入文件-->读取文件-->loads()组合起来，就可以永久化、传输。然而有更好的方法：
```python
# dump()序列化、存储到文件，一步到位。
with open(r'm.json', 'w+', ) as file: #encoding='utf-8'
    data = {'a': 1, 'b': 0.2, 'c': 'str', 'd': [1, 'm'], 'e': None, 'f': False}
    json.dump(data, file)
# 对应地，load()则是读取、解析到json，一步到位
with open(r'f.json',) as file:
    data = json.load(file)
    print(data, type(data))
```
- 如果要存储通用地转化、存储、解析Python的任何对象（内置对象、自定义类的实例），手动几乎不可能处理，需要拿起pickle、dbm、shelve模块。
```python
num_int = 1
dict_data = {"a": 1, "b": 0.2, "f": False, "d": [1, "m"], "c": "str", "e": None}
import pickle
bin_data = pickle.dumps(num_int)  # b'\x80\x03K\x01.'转为二进制数据
num = pickle.loads(bin_data)  # 1 <class 'int'> 转回Python对象
with open('data.pkl', 'wb+') as file:
    pickle.dump(dict_data, file) # 将Python对象写入文件
    # 将缓冲写入文件，然后将指针移动到文件的开始
    file.flush()
    file.seek(0)
    data = pickle.load(file)  # 从文件中解析出Python对象
    print(data, type(data))  # {'c': 'str', 'd'...} <class 'dict'>
```
还有其他文件类工具：标准流、Shell（os.open和subprocess.Popen产生shell命令，并且读取和写入到标准流）、os模块中有专门处理描述文件的工具、pipes、先进先出队列FIFO、套接字Socket、数据库接口对象、通过键访问文件、对象持久化、基于描述符的文件


