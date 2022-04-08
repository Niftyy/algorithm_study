# 1 2 3 4
# 1 1+2 1+2+3 1+2+3+4
# 1 1+1+2 1+1+2+1+2+3 1+1+2+1+2+3+1+2+3+4
# 1 1+1+1+2 1+1+1+2+1+1+2+1+2+3
ans = []
list_ans = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for i in range(1, 14 + 1): # 층 쌓기 -> 총 15층 (0~14)
    tmp = []
    for j in range(0, 14): # 호 쌓기 -> 총 14호 (0~13)
        if j == 0:
            tmp.append(1)
        else:
            sum = 0
            for k in range(j+1):
                sum += list_ans[i-1][k]
            tmp.append(sum)
    list_ans.append(tmp)

test_case = int(input())
for _ in range(test_case):
    sum = 0
    k = int(input())
    n = int(input())
    ans.append(list_ans[k][n-1])

for i in ans:
    print(i)