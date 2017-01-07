#-*-coding:utf-8-*-
from random import choice
yourscore = 0 # 你的得分
comscore = 0 # 电脑的得分
direction = ["left","center","right"]
print("Choose one side to shoot:\nleft OR center OR right")
your = input() # yourdirection
print("So you kicked \n"+your+"\n")
com = choice(direction) # Computer's direction
print("Computer saved "+com)

for i in range(0,5):
    print ("----Round %d - You Kick!----") %(i+1)
    print("Choose one side to shoot.")
    print("left OR center OR right")
    your = input() # yourdirection
    print("So you kicked "+your)
    com = choice(direction) # Computer's direction
    print("Computer saved "+com)
    if your != com :
        print ("Goal!")
        yourscore += 1
    else:
        print ("Oops...")
        
    print ("Score: %d(your score)--%d(computer's score')\n") %()




