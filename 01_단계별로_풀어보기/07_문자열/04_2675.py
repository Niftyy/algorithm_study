test_case = int(input())
n = []
s = []

for i in range(test_case):
    tmp1, tmp2 = list(input().split())
    n.append(int(tmp1))
    s.append(tmp2)

for i in range(test_case):
    for j in s[i]:
        print(j*n[i],end='')
    print()