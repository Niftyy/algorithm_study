test_num = int(input())
s=[]

for i in range(1, test_num+1):
    a, b = map(int,input().split())
    s.append(a+b)

for i in range(test_num):
    print(s[i])