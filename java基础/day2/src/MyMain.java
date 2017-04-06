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
class Employee{
    //成员变量
    int id;
    String name;
    Job job;
    Department dept;
    float salary;
    //构造方法 三个
    public Employee(int id,String name){
        this.id = id;
        this.name = name;
    }
    public Employee(int id,String name,Job job){
        this.id =id;
        this.name=name;
        this.job=job;
    }
    public Employee(int id,String name,Job job,Department dept){
        this.id = id;
        this.name = name;
        this.job = job;
        this.dept =dept;
    }
    //普通方法
    public void introduceMyself(){
        String str = String.format("我的工号是%d,我的名字叫%s",
                this.id,this.name);
        System.out.println(str);
    }
    //给成员变量salary赋值
    public void setSalary(float salary){
        this.salary = salary;
    }
    public float  getSalary(){
        return this.salary;
    }
}
class Department{
    int id;
    String description;
    String location;
    Employee manager;
    //构造方法
    public Department(int id,String description,String location){
        this.id = id;
        this.description = description;
        this.location = location;
    }
    //设置部门经理的方法
    public void setManager(Employee manager){
        this.manager.name = manager.name;
    }
}

public class MyMain {
    public static void main(String[] args){
        //创建一个员工（老板），工号100 名字Jack
        Employee boss = new Employee(100,"Jack");
        //创建一个职位，CEO，职位编号 90
        Job job1 = new Job(90,"CEO");
        //设置Jack的职位为CEO
        boss.job = job1;
        //创建一个部门，管理中心，部门编号 601，部门所在地 深圳
        Department dept = new Department(601,"管理中心","深圳");
        //设置Jack的部门为 管理中心
        boss.dept = dept;
        //设置管理中心的 部门经理 为Jack
        dept.manager = boss;
        //创建一个职位 研发工程师 91
        Job job2 = new Job(91,"研发工程师");
        //创建一个部门，产品研发部 602， 所在地是 深圳， 部门经理是 Jack
        Department dept2 = new Department(602,"产品研发部","深圳");
        //设置部门经理是 Jack
        dept2.manager = boss;
        //创建一个员工 工号101，名字 Smith，职位 研发工程师，部门 产品研发部
        Employee emp2 = new Employee(101,"Smith",job2,dept2);
        //设置Jack的工资为35000
        boss.setSalary(35000);
        //设置Smith的工资为25000
        emp2.setSalary(25000);
        System.out.println(dept2.id);
        System.out.println(dept2.description);
        System.out.println(dept2.location);
        System.out.println("产品研发部的经理是"+dept2.manager.name);
        //比较Jack的工资和Smith的工资，输出“Jack比Smith的工资高《多少具体值》，
        // Jack的工资是：Smith的工资是：”
//        if (boss.getSalary() > emp2.getSalary() ){
//            String str = String.format("Jack比Smith的工资高%f,Jack的工资是%f," +
//                    "Smith的工资是%f",(boss.getSalary() - emp2.getSalary()),boss.getSalary(),emp2.getSalary());
//            System.out.println(str);
//        }
        if(boss.salary > emp2.salary){
            String str = String.format("Jack比Smith的工资高%f,Jack的工资是%f,Smith的工资是%f",
                    (boss.salary - emp2.salary),boss.salary,emp2.salary);
            System.out.println(str);
        }
    }
}
