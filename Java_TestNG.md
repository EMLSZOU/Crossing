# TestNG教程

## 简介 Introduction
测试是检查应用程序的功能的过程是否按要求工作。单元测试是单一实体（类或方法）的测试。单元测试是非常必要的，何况当今已是测试驱动开发的时代，所以测试扮演重要角色。

比起其他测试框架，JUnit 凭借一个相当简单、务实、严谨的架构，一站式解决方案，带动了开发人员了解测试的实用性，推动了单元测试技术发展，开启了测试驱动的开发时代。JUnit 传扬的单元测试基本规则：
- 每段代码都必须经过测试。
- 只要有可能，代码的测试必须隔离进行。
- 软件必须容易测试 —— 也就是说，编码的时候要想着怎么去测试。

但是，在过去的几年中，JUnit 的改进不大。JUnit缺点：
- 最初仅为单元测试而设计，现在各种测试场景很多。如果要为复杂的环境编写测试代码，就必须把Junit和其他测试框架结合，这让测试越来越困难。
- 因为 Java 语言的单继承性，所以必须扩展 TestCase类的限制很大。
- 无法向 JUnit 的测试方法传递参数，也无法向 setUp()和 tearDown()方法传递参数。
- 执行模型有点奇怪：每次执行一个测试方法的时候，都要重新实例化测试类。
- 管理复杂项目中的不同测试套件有可能非常复杂。

TestNG是一个开源自动化测试框架。NG意为 Next Generation：它借鉴了JUnit和NUnit，尽量保留了它们的简单性，同时消除了大部分的旧框架的限制、引入了一些新的功能，功能更强大，使用更方便，使开发人员能够编写更加灵活和强大的测试。但它不是一个JUnit扩展，而是优于JUnit，尤其是当测试集成的时候。它的 TestNG的创造者是Cedric Beust（塞德里克·博伊斯特）
TestNG的特点：
- 可以在 TestNG 下用“兼容模式”运行过去运行良好的 Junit 测试。
- 用Java注解（JDK5.0引入的）定义测试，因此需要JDK5或更高的JDK版本
- 线程管理：测试可以运行在任意大的线程池中，并且有多种运行策略可供选择（所有测试方法运行在自己的线程中、每个测试类一个线程，等等）。线程安全。
- 灵活的测试配置、强大的运行模型（不再使用 TestSuite），支持综合类测试（例如，一般没有必要为每个测试用例创建一个被测类的实例）
- 支持数据驱动测试（通过 @DataProvider 注解），支持参数化
- 内嵌 BeanShell 以进一步增强灵活性
- 支持依赖测试、并行测试、负载测试、局部故障
- 涵盖所有类型的测试：单元，功能，端到端，集成等。
- 默认提供 JDK 的运行时和日志功能
- 有多种工具和插件支持（Eclipse, IDEA, Maven, 等等）

关于注解Annotations
由于TestNG是基于J2SE5.0的注解特性所构建的。注解是J2SE5.0所新提供的对于元数据的支持，作用：预编译指令(Compiler instructions)、编译时指令(Build-time instructions)、运行时指令(Runtime instructions)。开发人员可以在不改变原有逻辑的情况下，在源文件嵌入一些补充的信息，用来修饰类、接口、方法、方法参数、成员变量、局部变量等等。语法
```java
@Entity(tableName="vehile") @注解名(元素="元素值")。元素:元素值也可以称为属性:属性值。只有一个属性的时候，可以省略元素名，@Entity("vehile")
```
使用注解的好处：
- TestNG框架以@Test作为测试用例的标识，因此，和JUnit不同，TestNG中实现测试逻辑的类不需要继承任何父类，测试方法也无需遵循testXXX的命名规则。
- 我们可以通过额外的参数注解。
- 注解是强类型的，所以任何错误都会被编译器探测出来。

## 快速起步 Whetting Your Appetite
只要建立普通的java 类，用标注 @Test告诉TestNG框架这个方法是测试用力，再用assert来检测错误情况。
1. **TestNG安装**
    Eclipse：
    - 离线安装：TestNG Eclipse插件下载地址http://testng.org/doc/download.html。下载下来以后，放在eclipse的plugins文件夹下，然后启动eclipse，点击Help -> software update -> Installed Software, 查找到TestNG Eclipse插件，点击Install（安装），安装完成后，重启eclipse。然后去Windows -> show view -> other，Java文件夹下，有TestNG，双击图标，在eclipse界面下面便会出现TestNg的窗体。
    - 在线安装
        1. 选择菜单：Help->Install New Software，然后在弹出的窗口中的Work with后面的输入框中输入：http://beust.com/eclipse。
        2. 然后点击Add按钮，选中TestNG后一路点击Next下去安装即可，直到Finished之后，重启Eclipse完成安装。

   Intelij IDEA：IDEA 7及以上版本有相关插件，但是project里面没有添加相关的jar包，在相关的标记上（比如@Test）点击提示小灯泡，或者按快捷键 Alt Enter，然后选择Add ‘testng’ to class path，就可以了。
2. **最简单的例子：**
	这个用例没有涉及被测试的类。TestNG用法：import TestNG；在测试用例（方法）上标记 @Test ；用Assert.assertEquals(实际值，期望值，错误提示)作做检查，判断测试是否通过。
    一般来说，测试用例都写成void。但是即使有返回值，也会被TestNG忽略，如果不想被忽略，必须在xml里面加参数<suite allow-return-values="true">。
    ```java
    package learnTestNG;
    import org.testng.Assert;
    import org.testng.annotations.Test;
    public class TestDemo {
        @Test
        public void testDemo() {
            //Assert.assertEquals("actual", "expected","message");
            Assert.assertEquals(11, 12,"11 != 12");
        }
    }
    ```
    运行：“Run as TestNG test”，Eclipse 和 Intelij IDEA 都一样。
    结果：上半部分是一个个TestCase的报告，下半部分是一个TestSuite的报告。代码中设置的错误提示信息"11 != 12"已经生效
    ```javascript
    FAILED: TestDemo1
    java.lang.AssertionError: 11 != 12 expected [12] but found [11]
    ...
    ===============================================
        Default test
        Tests run: 1, Failures: 1, Skips: 0
    ===============================================
	```
    倘若，@Test标记一个类，那么这个类将会被识别为测试类，里面所有的方法都将被当做测试用例执行。
    ```java
    package learnTestNG;
    import org.testng.Assert;
    import org.testng.annotations.Test;
    @Test
    public class TestDemo {
        public void testDemo1() {Assert.assertEquals(11, 12,"11 != 12");}
        public void testDemo2() {Assert.assertEquals(0, 0,"0 != 0");}
    }
    ```
3. **被测试的类和方法**
	- 被测类 里面 包含 测试用例（方法）。对，这样也是可以的。但是，必须 “Run as TestNG test”
	```java
    package learnTestNG;
    import org.testng.Assert;
    import org.testng.annotations.Test;
    public class Calculate {
        public int add(int a, int b) {return a + b;}
        public int substract(int a, int b) {return a - b;}
        @Test
        public void testAdd(){
            Calculate cal = new Calculate();
            Assert.assertEquals(cal.add(6, 9), 16,"add(9,6) != 16");
            cal = null;
        }
    }
    ```
    - 测试用例 单独放在 测试类 里，被测试类 和 测试类 在同一个.java 文件里。如果 被测试类 和 测试类 不在同一个文件里，则需要 import
	```java
    package learnTestNG;
    import org.testng.Assert;
    import org.testng.annotations.*;//Before和Test之类
    public class CalculateTestng { //测试类
        private Calculate calculate; //声明变量。
        @BeforeClass  //JUnit里，fixture必须声明为static，而被测类的初始化必须public。TestNG都不需要
        public void beforeClass() { //测试之前运行的方法。初始化类
            System.out.println("this is before class");
            this.calculate=new Calculate();
        }
        @Test
        public void TestNg_Calculate_add() { //测试用例
            System.out.println("this is TestNG test case");
                Assert.assertEquals(calculate.add(6, 9), 16);
        }
        @AfterClass
        public void afterClass() {
            System.out.println("this is after class");
            this.calculate=null;
        }
    }
    class Calculate { //被测的类
        public int add(int a, int b) {return a + b;} //被测的方法
        public int substract(int a, int b) {return a - b;}
    }
    ```

##  注解 Annotations
**@Test：**让某个类成为测试类（所有方法都被当作测试用例），或者让某一个方法成为测试用例。参数：
- alwaysRun：如果设为 true，这个测试用例无论如何都会执行（即使依赖的方法失败了）。
- dataProvider：指定这个用例的数据源。
- dataProviderClass：这个用例的数据源，在那个类中？如果没有指定，就在本类或者父类中找。如果指定，数据源 方法，必须是static的。
- dependsOnGroups、dependsOnMethods：所依赖的测试组、用例。如果依赖方法失败，它将被跳过，而不是标记为失败。
- description:用例描述。
- enabled：这个测试类/测试用例是否执行。默认是true
- expectedExceptions：指定这个用例可能抛出的异常（一个列表）。如果发生指定范围之外的异常，这个用例就是failure。
- groups：用例所属的组。@Test(groups = {"tests.string"})
- invocationCount：这个用例最多引用多少次。
- invocationTimeOut：如果这个用例执行多次，那么总共执行时间不能超过多。
- priority：优先级。优先级低的用例将会先被执行。@Test(priority = 4,enabled=false)
- successPercentage：有多少把握这个用例能够通过。
- singleThreaded：如果设为 true，那么这个class里面的所有用例，将会在一个进程内执行，即使是某个用例已经被设为 parallel="methods"。
- timeOut：这个用例最多执行多少毫秒。
- threadPoolSize：这个用例的进程池大小。

**配置方法**
TestNG 中的配置方法是 JUnit 的 setUp()和 tearDown()方法的增强版；它们的主要目的是为测试创建正确的执行上下文，并在测试用例执行之后刷新数据。@Configuration已经被丢弃，而被下列方法取代。
@BeforeSuite 和 @AfterSuite: 被标注的方法，会在这个套件的所有方法执行之前（After是之后）执行。
@BeforeGroups 和 @AfterGroups: 被标注的方法，会在这个组的所有方法执行之前（After是之后）执行。@Test(groups = "")可以指定组。
@BeforeTest 和 @AfterTest: 被标注的方法，会在 xml <test>里面所有的类的方法运行之前（After是之后）执行。如果没有编辑xml，那么它和@beforeClass差不多。The annotated method will be run before any test method belonging to the classes inside the <test> tag is run.
@BeforeClass 和 @AfterClass: 被标注的方法，会在当前这个类的所有测试用例执行之前（After是之后）执行。
@BeforeMethod 和 @AfterMethod: 被标记的方法，会在**每个**测试用例执行之前（After是之后）执行。
参数：
- alwaysRun：对于@BeforeXXX（@BeforeGroups除外）：如果设为true，这个方法一定会执行，无论它属于哪个组。
- 而对于@AfterXXX 来说，这个方法一定会执行，无论前面的测试用例执行情况如何。
- dependsOnGroups 和 dependsOnMethods：依赖的 组/方法 列表。
- enabled：这个方法是否执行。
- groups：这个方法属于哪个组。
- inheritGroups：如果设为 true，这个方法只属于哪些将类标记为@Test的组。

**其他方法**
@DataProvider：将一个方法变成为测试用例提供数据的方法（数据源）。返回值必须是 object[][]，一个测试用例，会需要一组参数，那就组建一个object[]。
- name：名字要和测试用例指定的数据源名字对应。如果不设置，那就是方法名。
- parallel：默认值false。如果设为 true，测试用例将会平行使用这个方法。

@Factory：被标注的方法，将会变成一个factory，返回的对象会被TestNG用作 测试类。返回值必须是 object[]
@Listeners：定义测试类的 listeners。值是多个org.testng.ITestNGListener的子类，组建一个Array
@Parameters：描述怎样给测试用例传参。值是传给这个测试用例的参数列表。
@Configuration


##  定义xml文件：
启动一个 TestNG 测试项目，有3种方法：testng.xml、ant、命令行。
**TestSuite**
使用XML文件，通常命名为testng.xml配置TestNG。此文件的语法很简单，其内容如下。
-    ```HTML
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
    <suite name="Suite1" verbose="2"> 一个suite由参数、test构成。子级的参数会覆盖父级的参数。比如test覆盖suite。verbose="2" 记录的日志0-10级别，0表示无，10最详细
      <test name="test1"> 一个测试。可以由类、包、组构成。
        <classes> 定义由哪些类组建测试用例。可以只指定测试类，而不指定测试用例
            <class name="CalculateTestng">
                <methods> 一个个测试用例。一般很少这样做，主要目的是为了按照罗列的顺序执行。
                    <include name="TestNgLearn3" />被包含的用例
                    <include name="TestNgLearn1" />
                    <exclude name="TestNgLearn2" /> 不被包含的用例。
                </methods>
            </class>
        </classes>
        <packages> test也可以用package构建，而不是用class。
        	<package name="test.sample" />
		</packages>
	  </test>
    </suite>
    ```
用命令行启动测试：
如果 TestNG 在 class path 里，用命令行启动非常简单：
`C:\TestNG_WORKSPACE>java -cp "C:\TestNG_WORKSPACE" org.testng.TestNG testng.xml[testng2.xml testng3.xml ...]`

**TestGroup**
TestNG 另外一个有趣的特性是其定义测试组的能力。每个测试方法（测试类也可以）都可以与一个或多个组相关联，但可以选择只运行某个测试组。要把测试加入测试组，只要把组指定为 @Test标注的参数，使用的语法如下：
 @Test(groups = {"tests.string"}) //这个用例属于 tests.string组
因为参数 groups是一个数组，所以可以指定多个组，组名之间用逗号分隔，然后配置xml,有选择地运行它们。
如果你想一会儿运行这种组合，一会儿运行那种组合，groups是非常好的解决方案。
在 @Test 的时候定义 groups
- ```java
@Test(groups = { "checkin" }) //测试类可以定义
public class All {
  @Test(groups = { "func" ) //测试用例也可以定义。这个用例同时属于 "checkin" "func"两个组
  public void method1() { ... }
  public void method2() { ... }
}
```

在 xml中定义运行
- ```HTML
<!DOCTYPE suite SYSTEM "http://beust.com/testng/testng-1.0.dtd" >
<suite name="My suite">
    <test name="test2" preserve-order="false"> 默认按照xml文件列举顺序执行用例。如果不想这样，设置false
        <groups> 在测试类和用例上，定义group：@Test(groups={"brokenTests"})
            <run>
                <exclude name="brokenTests" /> 组名
                <include name="checkinTests" />
            </run>
        </groups>
        <classes> 同时和classes、packages并不冲突
            <class name="CalculateTestng"/>
        </classes>
    </test>
</suite>
```

甚至，还可以组建 groups of groups 组中组
- ```html
<test name="Regression1">
    <groups>
        <define name="functest"> 定义组：组functest包含2个用例
            <include name="windows" />
            <include name="linux" />
        </define>
        <define name="all"> 定义组：组all包含了 functest 和其他用例
            <include name="functest" />
            <include name="*.check.*" /> 正则匹配用例名，并不推荐，万一重构就不好办了
        </define>
        <run> 在这里指定运行。用<exclude name="broken"/>指定不运行
            <include name="all" />
        </run>
    </groups>
    <classes>
        <class name="test.sample.Test1" />
    </classes>
</test>
```
显然，当运行不同的测试组时，HTML 报告能够在单一列表中显示所有测试，也可以在独立的列表中显示每个组的测试，从而能够立即理解问题的来源。





##  异常机制
使用 TestNG，您可以非常简单、非常容易地检测异常的发生。@ExpectedExceptions指明能够容忍抛出的 NumberFormatException异常，所以不应当被当作是故障。要查看在某行代码中是否抛出异常，可以直接在这行代码之后加入 assert false语句。这意味着 只有在指定行中抛出特定类型的异常的时候，才会通过测试。
```java
 public class  NumberUtilsTest
 {
	 @Test(groups = {"tests.math"})
	 @ExpectedExceptions(NumberFormatException.class)
	 public void test()
	 {
		 NumberUtils.createDouble("12.23.45");
		 assert false;  //shouldn't be invoked
	 }
 }
```

```java
@Parameters({ "first-name" })
@Test
public void testSingleString(String firstName) {
  System.out.println("Invoked testString " + firstName);
  assert "Cedric".equals(firstName);
}
```

```html
<suite name="My suite">
  <parameter name="first-name"  value="Cedric"/>
  <test name="Simple example">
  <-- ... -->
```

## 与Ant
build.xml
- ```html
<project default="test">
    <path id="cp">
        <pathelement location="c:/spark/eclipse/plugins/org.testng.eclipse_4.7.0.0/lib/testng-jdk15.jar" />
        <pathelement location="c:\" />
    </path>
    <taskdef name="testng" classpathref="cp" classname="org.testng.TestNGAntTask" />
    <target name="test">
        <testng classpathref="cp" groups="HelloWorld, HelloNature">
            <classfileset dir="./" includes="example1/*.class" />
        </testng>
    </target>
</project>
```


## 运行结果
运行完成之后，会在运行目录下生成一个 test-output 目录。
该目录中包含有 html 形式的运行结果的报告，通过命令 start test-output\index.html 可以查看生成的测试报告。
该目录中有一个 testng-failed.xml 文件，该文件可以被用来运行前一次运行失败的所有测试用例。下文将会详细介绍使用该文件的步骤。
**重新运行前次运行失败的测试用例**
随着项目开发的进行，单元测试的数量也会成倍的增加。有时仅仅有数量很小的某几个测试用例会运行失败。在这种情况之下，对于每一次修改，可能并不需要跑完所有的测试用例。只需要重新运行前次运行失败的测试用例。TestNG 内建了重新运行上次失败测试用例的功能，下文将会给出重新运行前次错误测试用例的步骤。
运行一组测试用例，如果这一组测试用例中有失败的用例，TestNG 就会在输出目录中创建一个叫做 testng-failed.xml 的配置文件。这个文件记录了本组测试用例中运行失败的测试用例。使用该文件，用户可以快速的重新运行上次运行失败的测试用例。而无需运行整个测试用例组。如前文所述，运行完 Ant 脚本之后，会在脚本运行的目录之中生成一个 test-output 目录。该目录中，包含 testng-failed.xml 文件。可以用如下的命令运行被标记为运行失败的测试用例。
列表 3. 重新运行前次运行失败的测试用例
C:\>java -classpath
c:/spark/eclipse/plugins/org.testng.eclipse_4.7.0.0/lib/testng-jdk15.jar
org.testng.TestNG -d test-outputs test-output\testng-failures.xml

## 分布式运行、多线程支持
文章链接：https://www.ibm.com/developerworks/cn/java/j-lo-testng/

## 依赖测试 参数化、高级参数化
https://www.ibm.com/developerworks/cn/java/j-cq08296/




