li = []
for i in range(9):
    x = int(input())
    li.append(x)
mx = max(li)
print(mx)
print(li.index(mx)+1)