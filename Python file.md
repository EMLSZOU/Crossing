##文件 file
文件对象不是通过常量语法（比如 l = [1,2,3] ）创建的，而是调用 open() 函数创建的。
```python
#写入操作
    f = open('data.txt','w')  # (文件名，处理模式)
    f.write('Hello\n')  # 写入一行字符
    f.close()  # 关闭文件
#读取操作
    f = open('data.txt')  # 处理模式默认值为 'r'
    text = f.read()  # 读取文件内所有的内容（或者读取指定的字节数），存入变量
    print(text)  # 将内容打印
    f.close()  # 关闭文件
    text.split()  # 内容可以继续进行处理
    readline() 每次读取一行。seek() 移动到一个新的文件位置。
    #文件读取的最好的方式，是使用迭代器 iterator
#在Python3 中，文本与二进制的文件对象是截然不同的。
    f = open('data.txt')  # 文本文件，内容解析成字符串，默认执行Unicode编码
    f = open('data.bin','rb')  # 二进制文件，解析二进制
```
还有其他文件类工具：管道、先进先出队列FIFO、套接字Socket、数据库接口对象、通过键访问文件、对象持久化、基于描述符的文件


