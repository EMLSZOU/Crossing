from random import randint  # 引入模块。from 模块名 import 方法名
answer = randint(1,100)   # 模块中包含的函数randint,在1-100中取一个随机整数
print ("Guess what number I think? Input a number, please.")
user_answer = eval(   # Python3 的input==raw_input，加上eval()格式化
    input()           
)
while user_answer != answer: # 如果回答错了，就循环提问
    if user_answer > answer: # 两个if，针对不同的回答，给出不同的提示
        print ("Oh, your answer is too big. Input a smaller one, please")    
    if user_answer < answer:
        print ("Oh, your answer is too small. Input a bigger one, please")    
    user_answer = eval(
    input()
    )    # 再次输入
print ("You are smart, boy.")  #如果回答正确，退出循环提问