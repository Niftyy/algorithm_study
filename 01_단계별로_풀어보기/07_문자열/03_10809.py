from string import ascii_lowercase
alpha_list = list(ascii_lowercase)

s = list(input())
ans = []
for i in alpha_list:
    if i in s:
        ans.append(s.index(i))
        continue
    else: ans.append(-1)
for i in ans:
    print(i,end=' ')