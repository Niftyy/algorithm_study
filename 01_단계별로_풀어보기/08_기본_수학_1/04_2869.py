a, b, v = list(map(int, input().split()))

if (v-a)%(a-b) != 0:
    ans = (v - a) // (a - b) + 2
    print(int(ans))
else:
    ans = (v-a)/(a-b) + 1
    print(int(ans))