test_case = int(input())
s=[]

for i in range(test_case):
    num1,num2 = map(int,input().split())
    s.append(num1+num2)

for i in range(test_case):
    print("Case #{}: {}".format(i+1,s[i]))