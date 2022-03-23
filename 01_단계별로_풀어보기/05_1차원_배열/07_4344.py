t_num = int(input())
ans=[]

for i in range(t_num):
    up_p_num = 0
    p_num, *li = list(map(int,input().split()))
    avg_li = sum(li)/p_num
    for j in li:
        if j > avg_li:
            up_p_num+=1
    ans.append(up_p_num/p_num*100)

for i in ans:
    print(f"{round(i,3):.3f}%")