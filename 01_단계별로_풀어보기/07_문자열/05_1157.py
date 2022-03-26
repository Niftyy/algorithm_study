s = list(input().upper())
del_s = list(set(s))
ans = []
tmp = 0

for i in del_s:
    ans.append(s.count(i))
    if tmp <= s.count(i):
        tmp = s.count(i)
        char_a = i

if ans.count(max(ans)) != 1:
    print("?")
else:
    print(char_a)