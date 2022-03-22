a1, a2, a3 = map(int,input().split())

if a1==a2 and a2==a3:
    print(10000+a1*1000)
elif a1!=a2 and a2!=a3 and a1!=a3:
    print(max(a1,a2,a3)*100)
elif a1==a2 or a2==a3:
    print(1000+100*a2)
else:
    print(1000+100*a1)