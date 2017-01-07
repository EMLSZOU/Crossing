'''
# module模块。函数是重用自己程序内的代码。模块是重用别的程序的代码。
# 模块是一个包含了函数和变量的py文件。有很多官方标准库和第三方库。引入模块就可使用里面的类、方法、变量
import random  # import和from…import注意两者区别
a = random.randint(1, 10)
from random import randint  # 只是用到random的某一个函数
b = randint(1, 10)
print(a)
print(dir(random))
'''

# 文件导入、写入与程序
import os
from random import randint
if os.path.exists(r'game.txt'):  #
    f = open('game.txt', 'r+', encoding='gbk')
    score = f.read().split()  #
    f.close()
else:
    f = open('game.txt', 'w+', encoding='gbk')
    f.close()
    score = [0, 0, 0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times >0:
    avg_times = float(total_times)/game_times  # 如果不用float方法，结果四舍五入的为整数
else:
    avg_times = 0
print('你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(game_times, min_times, avg_times))

num = randint(1, 100)
times = 0
print('Guess and input a number,please')
bingo = False
while bingo == False:
    times += 1
    answer = eval(input())
    if answer < num:
        print('Too small!')
    elif answer > num:
        print('Too big!')
    elif answer == num:
        print('Bingo')
        bingo = True
if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
resault = '%d %d %d' %(game_times, min_times, total_times)
f = open('game.txt', 'w+', encoding='gbk')
f.write(resault)
f.close()