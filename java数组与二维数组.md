


<center>数组</center>
============
数组（array）是相同类型变量的集合和列表，使用共同的名字引用它。数组可以理解为是一个巨大的“盒子”，里面可以按顺序存放多个类型相同的数据。优点：避免声明和处理大量的同类变量。
##### 定义数组、分配空间、数组初始化：
数组是一种引用类型。变量指向引用的数组对象，数组对象中存放着数据，三者是不同的。对于变量来说，它的值只是数组对象，而不管里面有没有存放数据。
1. 声明：创建变量。决定组成数组的每一个基本元素的数据类型。声明后，变量的值为空，没有分配内存空间。
    ```java
    int[] scores; String[] names  //推荐这种写法 type[] var-name;
    int scores[]; String names[];  //不推荐这种写法  type var-name[]```
2. 赋值。
   要么用**指定的长度**创建数组对象，要么用**指定的数据**创建数组对象。
  - 分配空间（创建数组对象），然后一个个地存入数据。
    - 分配空间（设定数组的长度）：使用运算符new，分配出内存地址并且赋给变量（每个元素被初始化为零），这才成为实际的、物理上存在的数组。数组长度，指定数组中最多可存储多少个元素。
    - 存入数据：分配空间后就可以向数组中存放数据了。数组中的元素通过下标来访问，下标从 0 开始。
        ```java
        int scores;
        scores = new int[5];  //长度为5的整数数组 var-name=new type[size]
        scores[0] = 89;//指定整数数组scores的第一个元素的值为89```
   - 分配空间（创建数组对象），同时批量存入数据  new int[]{ 78, 93, 97, 84, 63 }
      ```java
      int scores;
      scores = new int[]{ 78, 93, 97, 84, 63 }; //常见于变量的再次赋值。```
3. 声明与赋值的步骤合并
	声明数组、分配空间可以同时进行，声明数组、分配空间、数组初始化也可以同时进行
   ```java
    int[] scores = new int[5]; //声明一个整数数组变量，赋值为长度为5的整数数组
    int[] scores = new int[]{ 78, 93, 97, 84, 63 };  // 这种方式常用于第二次赋值。
    int[] scores = { 78, 93, 97, 84, 63 }; // 这种简写方式，常用于初始赋值。
    ```
4. 错误例子
   ```java
    int[] score = new int[]; // 赋值错误：没有指定数组长度
    int[] score = new int[4]{90, 12, 34, 77}; //赋值错误：要么指定长度，要么指定数据
    int score = { 78, 23, 44, 78 }； //声明语法错误，应为int[] score
    ```

##### 访问元素
数组中的元素通过下标来访问，下标从 0 开始。scores[3] 表示数组中的第 4 个元素。数组下标的范围是 0 至 lenth-1 ，如果越界访问，就会报错。
- 最常见的是for 和 for each 遍历
- ```java
int[] ages = new int[] { 1, 2, 3, 4, 5 };
int[] tempArray = new int[] { 9, 8, 7, 6, 5, 4, 3 };
// 普通的for循环，ages.length 用于获取数组的长度
for (int i = 0; i < ages.length; i++) {
    ages[i] = tempArray[i + 1]; // 两个数组倒腾数据 {8, 7, 6, 5, 4}
}
// for each 循环，简单高效。结果： 8 7 6 5 4
for (int item : ages) {
    System.out.print(item + " ");
}
```

##### 使用 Arrays 类操作数组
Arrays 类是 Java 在 java.util 包中提供的一个工具类。该类中包含了一些方法用来直接操作数组，比如排序、搜索等。
对该数组的排序（按升序排列）语法：  Arrays.sort(数组名);
将一个数组转换成字符串，按顺序把多个数组元素连接在一起，多个元素之间使用逗号和空格隔开，语法：  Arrays.toString(数组名);
- ```java
public class ArrayType {
	public static void main(String []args){
		int[] tempArray = new int[] { 9, 8, 7, 6, 5, 4, 3 };
		Arrays.sort(tempArray);  // 用Arrays类的sort()方法排序。请注意：没有返回值
        String s = Arrays.toString(tempArray); //用Arrays类的toString()方法转成字符串
		System.out.println(s); // 结果： [3, 4, 5, 6, 7, 8, 9]
	}
}
```



<center>二维数组</center>
============
##### 定义数组、分配空间、数组初始化：
所谓二维数组，可以简单的理解为是一种“特殊”的一维数组，它的每个数组空间中保存的是一个一维数组。
那么如何使用二维数组呢，步骤如下：
1. 声明。
    ```java
    int[][] nums;  //数据类型[][] 数组名。 
    int nums [][]; //不太常见
    ```
2. 赋值。
  - 分配空间，然后一个个地存入数据。
    ```java
    int[][] nums;
    nums = new int[4][4]; // =new 数据类型[行数][列数]
    nums = new int[2][];  //如果不是规则数组，则先确定行数，然后每行指定长度（列）。
    nums[0] = new int[2]; //第一行，2列
    nums[1] = new int[3]; //第二行，3列
    nums[0][1] = 22;  // 存入数据的语法也类似。 数组名[行数][列数]=值；
    ```
  - 分配空间，同时批量地存入数据。
    ```java
    int[][] nums;
    nums = new int[][]{
        {1, 2, 3},
        {4, 5},
    };
    ```
3. 声明与赋值合并。
    ```java
    // 声明一个整数二维数组变量，并且分配空间5行4列。
    int[][] scores = new int[5][4];
    // 这种方式常用于第二次赋值。规则的二维数组。
    int[][] nums = new int[][] {{ 1, 2, 3 }, { 7, 8, 9 }};
    // 这种简写方式，常用于初始赋值。不规则的二维数组。
    int[][] ages = {{ 30 }, { 21, 25, 38 }, { 14, 28 }};
    ```
4. 错误例子
```java
int[][] num = new int[][5];
int[][] num = new int[][]; // int[][] num = new int [行数][列数]
System.out.println( num[5][] );  //访问必须指定具体的行数列数
```

##### 访问元素
与一维数组类似，array[row][rank]，先给出行的下标，然后给出列的下标。
- for 和 for each 遍历
遍历二维数组需要内嵌循环：
```java
int[][] ages = {{ 30 }, { 21, 25, 38 }, { 14, 28 }};
for (int j=0;j<ages.length;j++){ // for 循环
    for(int item: ages[j]){ // for each 循环
        System.out.print(item+" ");
    }
}
```
