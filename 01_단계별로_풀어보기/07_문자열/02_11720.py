num = int(input())
number = list(input())
number = list(map(int,number))
ans = 0
for i in number:
    ans += i
print(ans)