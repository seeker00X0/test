count=0
while count==0:
    score=input("请输入你的分数:")
    if score=='e':
        count=count+1
        break
    guess=int(score)

    if guess==100:
        print("S")
    else:
        if 90<=guess<100:
            print("A")
        if 80<=guess<90:
            print("B")
        if 60<=guess<80:
            print("C")
        if guess<60:
            print("D")
