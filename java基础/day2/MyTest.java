import sun.nio.cs.ext.SJIS_0213;

/**
 * Created by we on 16-9-9.
 */
/*
class sj{
    String name;
    public void sj(){
        System.out.println("我的名字叫"+ name +"我在设计,我设计完了");
    }
}
class WK{
    String name;
    public void WanKeng(){
        System.out.println(" "+name+" 在挖坑,坑挖好了没");
       System.out.println("陆涛在帮杨远丰挖坑,坑货还没有挖完!!");

    }
}


public class MyTest {
    public static void main(String[] args){
        sj sj1=new sj();
        sj1.name ="张欢";
        sj1.sj();
        WK wk = new WK();
        wk.name="杨丹";
        wk.WanKeng();
        WK wk1 = new WK();
        wk1.name="杨远丰";
        wk1.WanKeng();
    }
}
*/



//熊猫类

class Pandan{
     //成员变量
    String pandanName ="小妹";
    String address = "重庆";   //加成员变量
    //构造方法 用来做初始化工作,对象被创建的时候,构造方法会被自动调用
    public Pandan(String name,String addr){
             //加参数,再加参数
       System.out.println("这是构造方法,自动运行" );
        pandanName = "宝宝";
        pandanName = name;  //加参数名
        address = addr;    //加参数名
    }
    public Pandan(){
        System.out.println("这是一个无参数的构造方法");
    //这是一个无参数的构造方法
    }

    //普通方法
    public void  show(){
        System.out.println("这是一个普通方法,需要调用才能运行");
        System.out.println("我的名字是: " + pandanName +"我住在"+address);


    }
}
public class MyTest{
    public static void main(String[] args){
        String name = "xiaoming";
        String s = "shenzhen";
        System.out.println("我的名字叫:"+ name +"我住在:" +s);
           Pandan pan = new Pandan("宝宝" , "深圳"); //加参数 , 加地址参数
           pan.show();
           Pandan pan2 = new Pandan();
           pan2.show();
    }
}


