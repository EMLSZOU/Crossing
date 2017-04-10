# <center>Java String类</center>
字符串广泛应用在Java编程中，在Java中字符串属于对象，Java提供了String类来创建和操作字符串。
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
- String字符串的方法
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










