n, x = map(int,input().split())

num=[]
ans=[]

num = input().split()

for i in num:
    if int(i)<x:
        ans.append(i)

for i in ans:
    print(i,end=' ')