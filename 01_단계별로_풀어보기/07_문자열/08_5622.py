s = list(input().upper())
ans = 0
for i in s:
    n = 0
    for j in range(1, 8 + 1):
        if j ==6 or j==8:
            n += 4
        else:
            n += 3
        if ord(i)-64 <= n:
            ans += (j+2)
            break
print(ans)