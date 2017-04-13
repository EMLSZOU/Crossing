# <center>Java String类</center>
字符串广泛应用在Java编程中，在Java中字符串属于对象，Java提供了String类来创建和操作字符串。
String类：数据+相关的操作。String类的内部实现就是一个char[]，但是char数组只是数据，没有操作。
```java
String name = "Jhon"; //字面量"Jhon"，是String类型实例。
```
字符串常量表示语法:`public static final String TYPE = "car"`
字符串和字符可以相互转换。String字符串中的字符是有序号的，从0开始。
```java
String str = new String(new char[]{'1','2','3'});
char[] chs = str.toCharArray();```
String字面量相同时，会替换为同一个String对象的引用。

用于获取有关对象的信息的方法称为访问器方法。

- 连接字符串。String类提供了连接两个字符串的方法：
 	```java
    string1.concat(string2);  // "Hello ".concat("World!");
	string1 + string2;  // "Hello " + "World!"
    ```
- 创建格式化字符串。格式化输出可以使用printf()和format()方法。但用String类静态方法format()返回一个String对象而不是PrintStream对象，创建的是可复用的格式化字符串，而不仅仅是用于一次打印输出：
    ```java
    //语法
    String fs;
    fs = String.format("float %f, integer %d, string %s", floatVar, intVar, stringVar);
    System.out.println(fs);
    //例子
    String name ="zhangsan";
	int age =18;
	String str =String.format("you name is %s,you age is %d", name,age);
	System.out.println(str);
    ```
- String API（字符串的常用方法）
	- 字符串覆盖了equals()、hashCode()、toString()
    - String API 有一个实现原则：对象内容永远不变，也就是说String对象永远不变，这样的规定使字符串使用起来和基本类型相同。这些方法如果字符串有变化就返回新的String对象, 不变化就返回原字符串.  如: trim()
    | 方法名称 | 描述 |
    |--------|--------|
    | `s.length()` | 返回s字符串长度 |
    | `s.charAt(2)` | 返回s字符串中下标为2的字符。结果得到一个char|
    | `s.substring(0, 4)` | 返回s字符串中下标0到4的子字符串 |
    | `s.indexOf("Hello")` | 返回子字符串"Hello"的下标 |
    | `s.startsWith(" ")` | 判断s是否以空格开始|
    | `s.endsWith("om")` | 判断s是否以"om"结束 |
    | `s.equals("Good World!")` | 判断s是否等于"Good World!" |
    | `s.trim()` | 去掉s前后的空格，并返回新的字符串 |
    | `s.toUpperCase()` | 将s转换为大写字母，并返回新的字符串 |
    | `s.toLowerCase()` | 将s转换为小写，并返回新的字符串 |
    例子
    ```java
    public static void main(String args[]) {
    String name = "Jhon";
    int len = name.length();  // 结果为4
    char c = name.charAt(2);  // 结果为 'o'
    String str = name.substring(0,2);  // 结果为 "Jh"
    System.out.println(len+" "+c+" "+str); 
    int index = name.indexOf("ho");  // 结果为 1
    boolean startJ = name.startsWith("J");  // 结果为 true 
    boolean endk = name.endsWith("k");  // 结果为 false
    boolean equalsm = name.equals("make");  // 结果为 false
    System.out.println(index+" "+startJ+" "+endk+" "+equalsm);
    String myname = " Jim  ";  // 结果为
    String str1 = myname.trim();  // 结果为"Jim"
    String str2 = myname.toUpperCase();  // 结果为 " JIM  "
    String str3 = myname.toLowerCase();  // 结果为 " jim  "
    System.out.println(str1+" "+str2+" "+str3);
    }
    ```
Integer.parseInt()，转换到字符串到整数，如: "23"-> 23

**StringBuilder**
StringBuilder 和StringBuffer **
    String = char[] + 操作(复制创建新对象) char[]不可变
    StringBuilder = char[] + 对char[]操作(处理当前数组内容) char[]可变
    StringBuilder 内部的char[]数组内容可变，如果长度不够，利用变长算法维护，自动扩容长度。
    1) StringBuilder 是变长字符序列 
    2) StringBuilder 方法：append，insert ... 都返回当前 StringBuilder 对象本身的引用 
    3) 如果软件需要大量字符串处理时候建议使用StringBuilder 
    4) String s = s1+s2; Java 实际上是如下代码运行： 
    String s=new StringBuilder(s1).append(s2).toString(); 
append()方法，表示“追加”，该方法反复操作的始终是1个对象
insert()方法，表示“插入”
delete()方法，表示“删除”

String s = s1+s2+s3+s4; 被优化为 String s = new StringBuilder(s1).append(s2).append(s3).append(s4).toString(); 
s += "a"会产生两个新对象(StringBuilder, String)（笔试题） 
StringBuilder buf=new StringBuilder(); 
buf.append("a"); 

StringBuffer 和 StringBuilder API 几乎一样！
StringBuffer 是java 早期提供的（JDK1.0），速度稍慢，线程安全 
StringBuilder 是Java5 以后提供的（JDK5.0），速度快，非线程安全 

. s += "A";相当于s = new StringBuilder(s).append("A").toString，每当做一次字符串拼接，就会创建一个StringBuilder 新对象，同时JVM 在适时回收这些对象，如此会严重影响性能 
结论：当处理少量字符串拼接时使用String s = "a"+"b"，大量字符串拼接操作时StringBuilder， 
   如果对字符串性能有极高要求，则直接操作char[]数组 








<center>正则表达式</center>
===
String 对正则表达式的支持，重点掌握如下3个方法： 
   matches() 匹配正则表达式 
   split(“[,\s\|]”) 切分字符串为字符串数组 
   replaceAll() 替换字符串




正则表达式以“^”开头，“$”结尾
##### 字符集
```
[1234] 表示  1,2,3,4 之一
[^12]  表示除了  1,2
[1-5] 表示  1,2,3,4,5
[a-f] 表示  a-f 之间的
[0-9a-fA-F] 表示一个16进制字符
0[xX][0-9a-fA-F]{1,8} 表示整数的16进制数表达式
[\w-]{8,15} 表示8-15个字符、下划线、数字及“-”
```
##### 预定义字符集
```
\d 表示[0-9]
“.”点  表示任意字符
 \w 表示单词字符  [0-9a-zA-Z_] 注：包含下划线“_”
 \s 表示匹配空白: \t \n \r \b \p
\D （不常用）表示非数字 [^0-9]
\S （不常用）表示非空白
\W （不常用）表示非单词字符  [^0-9a-zA-Z_]
{m,n} 表示数词m到n个
{n} 表示数词n个，比如表示“5个以上”用{5,}
? 表示能出现0到1次  {0，1}
+ 表示能出现1到n次  {1，}
* 表示能出现0到n次  {0，}
```
##### 常用正则表达式写法

邮政编码——0-9的任意数字可出现6次
`^[0-9][0-9][0-9][0-9][0-9][0-9]$`
还可以写成 `^[0-9]{6}$`
或者  ` ^\d{6}$ `

用户名规则：可出现9-11个单词或字符
`^[a-zA-Z]\w{8,10}$  `

电话号码:  +86 13912345678  "+"特殊字符，需要转义"\+"表示"加号"
    ```^(\+86|0086)?\s?\d{11}$
  	\+86 表示出现"\+86"这几个字符
	(\+86|0086)? 表示“+86”或"0086"出现 0-1次
	\s? 表示空白(空格)出现0-1次
	\d{11} 表示出现11位数字```

身份证号码:` ^\d{15}(\d{2}[0-9xX])?$ \d{17}[0-9xX]`
一个点的坐标 ` ^\d+(,\s*|\s+)\d+$`
【解释】  \d+ 表示出现1个及以上的数字 ，(,\s*|\s+) 表示出现“逗号和0个及以上的空白”或者“1个以上的空白”
\d+ 表示出现1个及以上的数字

`^\s*A?(\s+|,\s*)B?(\s+|,\s*)C?(\s+|,\s*)D?\s*$ `
【解释】  \s* 可出现0-n个空格
A? A可出现0-1次
(\s+|,\s*) “1个以上空白“或"逗号，0个及以
上空白“
 D?\s*

日期 2011-01-30
	`^\d{4}-\d{2}-\d{2}$  `
	`^\d{4}(-\d{2}){2}$  `
IP 地址  192.168.0.2
	` ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$  `
	`^\d{1,3}(\.\d{1,3}){3}$  `
	`^(\d{1,3}\.){3}\d{1,3}$` “.”是特殊字符，需要转义“\.”
电话号码可能有3-4位区号0415-5561111 
   ` ^\d{3,4}-\d{7}$`
邮箱：
   `^\w{15}@\w+\\. (com|com.cn){1}$`



<center>Input 与 Output</center>
===

### 输出
输出很简单。
不换行  `System.out.print("How old are you?");`
换行   `System.out.println("How old are you?");`
格式化   `System.out.printf("My name: %s, age: %d", "Jhon", 18);`
格式化输出是一整套C-like的语法，比较复杂。

### 输入
输入会比较麻烦。先创建一个实例，然后调用方法。
如果要输入密码，因为不能显示出来，还要使用 console()
    ```java
	public static void main(String[] args) {
		Scanner input  = new Scanner(System.in);
		System.out.print("What is your name?");
		String fullName = input.nextLine(); //換行作為終止符
		System.out.print("How old are you?");
		int age = input.nextInt();
		System.out.printf("My name: %s, age: %d",fullName,age);
		//Scanner 类不适合读取密码。而是用Console类。
		Console con = System.console();
		//static String readLine()
		String username= con.readLine("Username: ");
		// static char[] readPassword()
		char[] passwd = con.readPassword("Password: ");
	}
    ```
### 文件输入
	```java
    Scanner fileIn = new Scanner(Paths.get("C:\\directory\\test.txt"));
    String fullName = fileIn.nextLine();  //就可以用很多Scanner的方法了
    ```
### 文件输出
	```java
    //创建一个写入对象。如果文件不存在，那就创建这个文件。
    PrintWriter fileOut = new PrintWriter(Paths.get("C:\\directory\\test.txt"));
    fileOut.println("Hello World");  //就可以用很多System.out.println()之类的方法了
    ```










