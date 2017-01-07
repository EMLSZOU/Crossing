#coding:UTF-8
# 等差数列求和，用高斯方式，首末项相加，检验编程和逻辑思维
from random import randint  # 引入模块。from 模块名 import 方法名
n = randint(1,100)   # 模块中包含的函数randint,在1-100中取一个随机整数
d = randint(1,100)
a1 = 1
an = a1 + (n-1) * d
Sn = n * a1 + n * (n-1) * d /2      # 数列公式求和
a = 0           # 自增的初始值
if (n %2) == 0:  # n为偶数的数列求和
    print ("n为偶数,a1=1, d=%s, n= %s , Sn= %s.") %(d,n,Sn)
    while a < n/2 + 1 :  # 循环累加n/2次
        Sna = 0
        Sna = (a1+a*d) + (an-a*d)
        a = a + 1
    if Sna == Sna :
        print ("Sn= %s = Sna, Your program is great!") %(Sn)
    else  :
        print ("Sn= %s , Sna= %s, Sn≠Sna, Sorry,your program is Failed!") %(Sn, Sna)
else:   # n为奇数的数列求和
    print ("n为奇数,a1=1, d=%s, n= %s , Sn= %s.") %(d,n,Sn)
    while a < n/2 :
        Sna = 0
        Sna = a1  + an + Sna
        a = a + 1
    Sna = Sna + (n-1)*d/2
    if Sna == Sna :
        print ("Sn= %s = Sna, Your program is great!") %(Sn)
    else  :
        print ("Sn= %s , Sna= %s, Sn≠Sna, Sorry,your program is Failed!") %s(Sn, Sna)