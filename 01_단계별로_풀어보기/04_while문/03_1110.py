num = int(input())

ans = num
cnt = 1

# a+b=c
while True:

    a = num // 10
    b = num % 10
    c = a + b

    num = 10 * b + c % 10
    if ans == num:
        break
    cnt += 1

print(cnt)


# 55 5+5=10
# 50 5+0=5
# 05 0+5=5
# 55

# 26 2+6=8
# 68 6+8=14
# 84 8+4=12
# 42 4+2=6