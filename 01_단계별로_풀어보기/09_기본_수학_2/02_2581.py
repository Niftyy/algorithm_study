m = int(input())
n = int(input())
sum = 0
ans = []

for i in range(m,n+1):
    for j in range(2,i+1):
        if j==i:
            sum+=i
            ans.append(i)
        if i%j ==0:
            break
if sum==0:
    print(-1)
else:
    print(sum)
    print(ans[0])