"""     用Pyhon设计第一个游戏   """
import random
answer=random.randint(1,10)

counts=3
while counts>0:
    temp=input("不妨猜一下我现在想的是哪个数字：")
    guess=int(temp)

    if guess==answer:
        print("猜对了~")
        print("对了也没奖")
        break
    else:
        if guess<answer:
            print("小啦~")
        else:
            print("大啦~")
    counts=counts-1

print("游戏结束，不玩啦~")
