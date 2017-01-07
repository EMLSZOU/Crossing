#-*-coding:utf-8-*-
#第一次定义及使用函数
def youright(num1,num2):
    if num1<num2:
        print ("Your answer is too small. Input another, please.")
        return False;
    if num1>num2:
        print ("Your answer is too big. Input another, please.")
        return False;
    if num1==num2:
        print ("Bingo. You are right.")
        return True

from random import randint
num = randint(1,100)
print ("Guess what I think and input a number.")
check = False
while check==False:
    answer = eval(input())
    check = youright(answer,num)