a = int(input())
b = int(input())
c = int(input())
li = [0,0,0,0,0,0,0,0,0,0]
num = a*b*c
num = str(num)

for i in range(10):
    for j in num:
        if i == int(j):
            li[i]+=1

for i in range(10):
    print(li[i])