# -*- coding: utf-8 -*-
print(list(range(1, 10)))  # list函数将range()转换为list[1,...,9]

l = [1, 1, 2, 3, 5, 8, 13]
print(l)  # 结果为：[1, 1, 2, 3, 5, 8, 13]
for i in l:
    print(i, end=',')  # end指明结尾，不换行。结果为：1,2,3,4,5,6,7,8,9,
print()

l = [365, 0.618, 'fish', True]  # 一个列表可以包含不同类型的变量
print(l[0])  # 访问列表。索引以0开始，不准越界
l[2], l[3] = False, 'Cat'  # 替换列表内的元素
l.append(9.322e-36j)  # 末尾增加一个复数元素
print(l)  # 结果5个元素：[365, 0.618, False, 'Cat', 9.322e-36j]
del l[2]  # 删除第3个元素。del l[2:6]指的是第3—5个元素，并没越界
print(l)
del l[1:3]  # 删除第2、3个元素。而不是第2、3、4个元素。
print(l)

# 26.list
from random import choice
score_you = 0
score_com = 0
direction = ['left', 'center', 'right']
for i in range(5):
    print('---------------- Round %d - You Kick! -----------------' % (i+1))
    print('Choose one side to shoot:\nleft, center, right')
    you = input()
    print('You kicked '+you)
    com = choice(direction)
    print('Computer saved '+com)
    if you != com:
        print('Goal!')
        score_you += 1
    else:
        print('Oops...')
    print('Score: %d(You):%d(Computer)\n' % (score_you, score_com))

    print('---------------- Round %d - You Save! -----------------' % (i+1))
    print('Choose one side to save:\nleft, center, right')
    you = input()
    print('You saved '+you)
    com = choice(direction)
    print('Computer kicked '+com)
    if you == com:
        print('Saved!')
    else:
        print('Oops...')
        score_com += 1
    print('Score: %d(You):%d(Computer)\n' % (score_you, score_com))



