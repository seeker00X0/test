import random

counts=input("请输入抛硬币的次数:")
counts=int(counts)
i = 0

print("开始抛硬币实验：")
while i < counts:
    num=random.randint(1,10)
    if num % 2:
        print("反面")
    else:
        print("正面")

    i = i + 1
