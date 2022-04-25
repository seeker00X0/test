weith=input("请输入今年的利润：")
weith=int(weith)
if weith<=100000:
    print("应该发放的奖金总数是:",weith*10/100)
elif weith>100000 and weith<=200000:
    print("应该发放的奖金总数是:",10000+(weith-100000)*7.5/100)
elif weith>200000 and weith<=400000:
    print("应该发放的奖金总数是:",17500+(weith-200000)*5/100)
elif weith>400000 and weith<=600000:
    print("应该发放的奖金总数是:",27500+(weith-400000)*3/100)
elif weith>600000 and weith<=1000000:
    print("应该发放的奖金总数是:",33500+(weith-600000)*1.5/100)
elif weith>1000000:
    print("应该发放的奖金总数是:",39500+(weith-1000000)*1/100)
