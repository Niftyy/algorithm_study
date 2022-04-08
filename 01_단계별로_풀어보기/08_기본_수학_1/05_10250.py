test_case = int(input())
ans = []

for i in range(test_case):
    h, w, p_num = list(map(int, input().split()))
    floor = p_num % h
    r_num = (p_num) // h + 1
    if floor == 0:
        floor = h
    if p_num % h == 0:
        r_num = (p_num) // h
    floor = str(floor)
    if r_num < 10:
        r_num = '0' + str(r_num)
    else:
        r_num = str(r_num)
    ans.append(floor + r_num)

for i in ans:
    print(i)