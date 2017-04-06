/**
 * Created by we on 16-9-10.
 */
//import boy.Pandan;
//
//public class MyTest{
//    public static void main(String[] args){
//        String name = "xiaoming";
//        String s = "shenzhen";
//        System.out.println("我的名字叫:"+ name +"我住在:" +s);
//           Pandan pan = new Pandan("宝宝" , "深圳"); //加参数 , 加地址参数
//           pan.show();
//           Pandan pan2 = new Pandan();
//           pan2.show();
//    }
//}


    //工作种类
class Job{
    int id;
    String title;
    //构造方法
 public Job(int id,String title){
     this.id = id;
     this.title = title;
    }
 }

   //员工类
class Employee {
       //成员变量
       int id;
       String name;
       Job job;
       Department dept;
       float salary;
       //构造方法 三个
       public Employee(int id, String name) {
           this.id = id;
           this.name = name;
       }

       public Employee(int id, String name, Job job) {
           this.id = id;
           this.name = name;
           this.job = job;
       }

       public Employee(int id, String name, Job job, Department dept) {
           this.id = id;
           this.name = name;
           this.job = job;
           this.dept = dept;
       }


       public void introduceMyself() {
           String str = String.format("我的员工号是%d,我的工作是%s,我所在的部门是%s",
                   this.id,this.name,this.job,this,dept );
           System.out.println();
       }
          //给成员变量salary赋值
       public void setSalary(float salary) {
           this.salary = salary;
       }
       public float getSalary() {
           return this.salary;
       }
   }
    class Department {
        int id;
        String description;
        String location;
        Employee manager;
          //构造方法
        public Department(int id, String description, String location) {
            this.id = id;
            this.description = description;
            this.location = location;
        }
        //设置部门经理的方法
public void  setManager(Employee manager){
         this.manager.name=manager.name;
      }
}
public  class MyTest {
    public static void main(String[] args) {
//        Employee emp1 = new Employee(100, "Jack");
//        emp1.job.title = "laoban";
//        Employee job1 = new Employee(90, "CEO");
//        emp1.job.title = "CEO";

        //创建一个员工(老板)

    }
}