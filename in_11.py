# -*- coding: utf-8 -*-
# 11.logic
a = 1<3
b = 2==3
c = False
d = b == False
e = not c
f = c != e
g = c and e
h = c or e
print(a, b, c, d, e, f, g, h)

# 12.for循环  # 15.for into for
for i in range(0, 6):  # for循环，遍历1,2,3,4,5
    print(i)
print(i)  # i的值为5

for i in range(0, 5):
    print('*', end=' ')
print('i=%d' % i)

for i in range(0, 5):
    for j in range(0, 5):
        print(i, j)
print('i=%d,j=%d' % (i, j))

for i in range(0, 5):
    for j in range(0, 5):
        print('*', end='')
    print()

for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end='')
    print()



# 14.string  16.string
str1 = 'My age is'
str2 = 'eighteen'
num = 18
print(str1+str2)  # 字符串连接
print(str1+str(num))  # 用str()函数转成字符串
print(str1, num)  # 用str()函数转成字符串，逗号会加字符串
print('My age is %d' % num)  # 字符串格式化
name, score = 'Lily', 95
print("%s's score is %d" %('Mike', score))  # 字符串格式化。有变量。有元组
print("%s's score is %d" %(name, score))  # 字符串格式化。有变量。有元组

# 17.Var trans
print('Hello'+str(1))
print('Hello%d' % int('db'))
int('db') == 123
float('3.333') == 3.333
str(111) == '111'
bool(0) == False

# 19.Function
def sayHello1():  # 不带参数的函数
    print('Hello World!')
def sayHello2(someone):  # 带参数的函数
    print(someone ,'Says Hello!')
def sayHello3(someone = 'Jhon'):  # 带默认参数的函数
    print(someone ,'Says Hello!')
sayHello1()  # 调用不带参数的函数，必定不传入参数
sayHello2('Jhon')  # 调用带参数的函数，必定要传入参数
sayHello3()  # 调用带有默认参数的函数，可以传入参数，也可以不传入
sayHello3('Coral')


def plus(num1, num2):
    print(num1+num2)
sayHello1()
sayHello2('aChing')
x, y = 3, 5
plus(x, y)

def isEqual(num1, num2):  # input,com
    if num1 > num2:
        print('too Big!')
        return False
    elif num1 < num2:
        print('too Small!')
        return False
    elif num1 == num2:
        print('Bingo')
        return True
from random import randint
com = randint(1,100)
print('Guess what I think? Input a number.')
bingo = False
while bingo == False:
    humman = eval(input())
    bingo = isEqual(humman, com)
print('Over')