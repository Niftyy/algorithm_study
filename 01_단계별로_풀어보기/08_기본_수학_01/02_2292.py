n = int(input())
tmp = 1
cnt = 1

while True:
    if n<=tmp:
        print(cnt)
        break
    tmp+=6*cnt
    cnt+=1