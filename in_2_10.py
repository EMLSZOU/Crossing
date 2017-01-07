from random import randint

# 2.print
print('Hello world!')  # 在Python命令行里，print()可以省略
print(40)
print(3.14)
print(3e30)  # 3e+30
print(1 + 2 * 3)  # 运算
print(2 > 5)  # boolean

# 4.input()
print('Who do you think I am?')
answer = input()  # 2与3的语法区别。eval(input())
print('Oh, yes!')
del answer

# 5.变量
var1 = 123.456
print(var1)
var1 = 'Hello'
print(var1)
print('Who do you think I am?')
your_answer = input()
print('Oh, yes! I am a')
print(your_answer)
del var1, your_answer

# 6.布尔值
# 7.if
print('这是真爱吗，输入True或者False')
thisIsLove = input()
if thisIsLove:
    print('再转身就该勇敢留下来')
#*************************
num = 10
print('Guess what I think?')
answer = eval(input())
if answer < num:
    print('Too small')
if answer == num:
    print('BINGO')
if answer > num:
    print('Too big')
del thisIsLove, answer, num

# 8.while
a = 1
while a != 0:
    print('Please input a number,then iput 0 in next time')
    a = eval(input())
print('Over')
del a

# 9.random

num = randint(1, 100)  # 闭区间[1,10]取随机整数
print('Guess what I think?')
answer = 0.1  # 先赋一个小数值，就不与num相等了
while answer != num:
    answer = eval(input())
    if answer < num:
        print('Oh, your answer is too small! Please input another one!')
    elif answer > num:
        print('Oh, your answer is too Big! Please input another one!')
    else:
        print('BINGO!')
del num, answer

# 10.variaty 2
# 高斯100累加求和
a, b = 1, 100
sumup = 0
while a<51:
    sumup = sumup + a + b
    a = a+1
    b = b-1
print(sumup,'over')
del a, b, sumup

# a1=1,d=1,n=ramdint，Sn=n*a1+n(n-1)d/2
a1 = 1
n = randint(1, 100)
print('n为', n)
an = n
sn = n+n*(n-1)/2
sumup = 0
while a1 <= (n/2):
    sumup = sumup + a1 + an
    an -= 1
    a1 += 1
if n%2 == 1:
    sumup = sumup + a1
print('累加求和', sumup, '等差求和', sn)
del a1, n, an, sumup


# a1=randint,d=randint,n=randint，Sn=n*a1+n(n-1)d/2
a1 = randint(1, 10)
d = randint(1, 10)
n = randint(1, 100)
an = a1 + (n-1)*d
sn = n*a1+n*(n-1)*d/2
print('a1为', a1, '，d为', d,  '，n为', n, 'an为', an, '，等差求和公式sn为', sn)
sumup = 0
count = 1  ################一定要注意计数count的开始值
while count <= (n/2):
    sumup = sumup + a1 + an
    an = an - d
    a1 = a1 + d
    count += 1
if n%2 == 1:
    sumup = sumup + a1
print('累加求和', sumup, '等差求和公式sn', sn)
del a1, n, an, sumup