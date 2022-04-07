n = int(input())
ans = -1
for i in range(3):
    if n - (5*i) < 0:
        break
    if (n - (5*i)) % 3 == 0:
        ans = (i + ((n - 5*i) // 3))
for i in range(5):
    if n - (3*i) < 0:
        break
    if (n - (3*i)) % 5 == 0:
        ans = (i + ((n - 3*i) // 5))
print(ans)