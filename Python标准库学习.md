# Python标准库

选出标准库3方面的包：

- Python增强：文字处理（string，textwrap，re）、数据结构（array、Queue、copy）、日期和时间（date、time）、数学（Decimal、Fraction、math、random、numpy）、存储（pickle、各种数据库）
- 操作系统：Python自身的运行sys、操作系统os、命令行subprocess、进程与线程threading/multiprocessing
- 网络：底层socket、互联网应用（request等等）

## 一、Python增强

### re模块

正则表达式(regular expression，或称Regex，或称RE)主要功能通过特定的模式(pattern)，是从字符串(string)中搜索想要找到的内容，然后取出或者替换。

分为2部分：正则表达式语法，re模块的接口调用。
###### 例1  第一个示例，正则三步走：创建正则对象，搜索，解析

```python
import re  # 导入模块
regex_obj = re.compile(r'\d\d\d-\d\d\d\d')  # 创建一个_sre.SRE_Pattern类的正则对象。注意用r字符串
match_obj = regex_obj.search('Phone: 137-6773')  # 调用search方法，返回一个_sre.SRE_Match类的对象。如果没有匹配，返回None，使用group()函数就会Error
# match_obj = re.search(r'(\d\d\d)-(\d\d\d\d)', 'Phone: 137-6773') 也可以两步合并为一步
num_str = match_obj.group()  # 解析出字符串
```

###### 例2  分组（）

```python
import re  # 导入模块
regex_obj = re.compile(r'(\d\d\d)-(\d\d\d\d)')  # 用括号分组
match_obj = regex_obj.search('Phone: 137-6773')
num_str = match_obj.group(0)  # 不传入参数，或者传入0，获得整个匹配
print(num_str) # 137-6773
num_str1 = match_obj.group(1)  # 传入1，就获得1组的结果
print(num_str1) # 137
area_code, main_num = match_obj.groups()  # groups返回所有分组的元组
```

###### 例3  管道 |

```python
regex_obj = re.compile(r'Jhon|Lennon')  # 用 | 分割。可以用 \| 转义
name = regex_obj.search('Jhon is tall.').group() # Jhon，出现其中一个，就能匹配
name = regex_obj.search('Lennon is tall.').group() # Lennon
name = regex_obj.search('Jhon Lennon is tall.').group() # Jhon 都出现时，就返回最先匹配的那个
# 如果开头都一样，还可以使用分组。比如匹配Adidas、Armani、Asos、Apple
regex_obj = re.compile(r'Adidas|Armani|Asos|Apple') # 管道
regex_obj = re.compile(r'A(didas|rmani|sos|pple)') # 管道 + 分组
```

###### 例4   次数指定：？和 * 和 + 和 {n}

```Python
# ?符号表示可选，前面的字符/组可以出现0次或者1次
regex_obj = re.compile(r's?ome')  # 匹配some、ome，但不匹配ame
regex_obj = re.compile(r'(so)?me')  # 分组。匹配some、me，但不匹配ame
# *符号表示可选、可重复，前面的字符/组可以出现0次或者n次
regex_obj = re.compile(r's*ome')  # 匹配ome、some、ssome，但不匹配ame
regex_obj = re.compile(r'(so)*me')  # 分组。匹配me、some、sosome，但不匹配ame
# +符号表示必需、可重复，前面的字符/组可以出现1次或者n次
regex_obj = re.compile(r's+ome')  # 匹配some、ssome，但不匹配ome、ame
regex_obj = re.compile(r'(so)+me')  # 分组。匹配some、sosome，但不匹配me、ame
# {}可以指定特定次数
regex_obj = re.compile(r'so{2}')  # 匹配'soo'，但不匹配'so'
regex_obj = re.compile(r'(so){1,2}')  # 指定最小最大的次数。匹配'so'和'soso'
regex_obj = re.compile(r'(so){,2}me')  # 指定最大值，匹配0-2次实例。匹配'me'和'some'和'sosome'
regex_obj = re.compile(r'(so){1,}me')  # 指定最大值，匹配1-n次实例。相当于 (so)+me
# 贪心和非贪心匹配。当能匹配的次数不确定的时候
result = re.search(r'(so){1,2}', 'soso').group()  # soso 默认是贪心匹配，越多越好
result = re.search(r'(so){1,2}?', 'soso').group()  # so 用?指定非贪心匹配(这种作用和表示可选，是没有关系的)
```



| Regex | 含义                    |
| ----- | --------------------- |
| `?'   | ``匹配some、ome，但不匹配aome |
|       |                       |
|       |                       |