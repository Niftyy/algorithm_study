test_case = int(input())
a1=[]
a2=[]
s=[]

for i in range(test_case):
    num1,num2 = map(int,input().split())
    a1.append(num1)
    a2.append(num2)
    s.append(num1+num2)

for i in range(test_case):
    print("Case #{}: {} + {} = {}".format(i+1,a1[i],a2[i],s[i]))