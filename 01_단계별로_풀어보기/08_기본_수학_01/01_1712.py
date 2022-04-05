a, b, c = list(map(int, input().split()))

if (c - b) <= 0:
    print(-1)
else:
    print((a//(c-b))+1)