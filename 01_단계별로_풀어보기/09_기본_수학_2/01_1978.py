n = int(input())
n_list = list(map(int,input().split()))

ans = 0

for i in n_list:
    if i == 1:
        pass
    elif i == 2:
        ans+=1
    else:
        for j in range(2,i+1):
            if i == j:
                ans +=1
            if i % j == 0:
                break
print(ans)
