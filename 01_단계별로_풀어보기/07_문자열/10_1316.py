num = int(input())
s=[]
answer = 0
for i in range(num):
    s.append(list(input()))

for i in range(num):
    ans = []
    for j in range(len(s[i])):
        if j == 0:
            ans.append(s[i][j])
        elif s[i][j-1] != s[i][j]:
            ans.append(s[i][j])
    if len(ans) == len(set(ans)):
        answer+=1

print(answer)