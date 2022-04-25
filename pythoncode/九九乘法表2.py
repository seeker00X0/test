for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end=' ')
        j+=1
    print()
    i+=1
