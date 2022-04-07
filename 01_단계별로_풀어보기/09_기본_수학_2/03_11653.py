n = int(input())
ans = n

while True:
    for i in range(2,n+1):
        if ans % i == 0:
            ans = ans//i
            print(i)
            break
    if ans==1:
        break
