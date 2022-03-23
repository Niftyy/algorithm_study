n = int(input())
li=[]
ans = []
for i in range(n):
    num_check = 0
    tmp = []
    li.append(str(input()))
    tmp = li[i].split('X')
    for j in tmp:
        num_check += (1 + len(j))/2*len(j)
    ans.append(num_check)

for w in ans:
    print(int(w))