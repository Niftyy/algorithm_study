def change_list(num):
    li = list(str(num))
    li = list(map(int, li))
    return li

def check_han(li):
    if li[1]-li[0] == li[2]-li[1]:
        return 1
    else: return 0

inp = int(input())
sum = 0

if inp<100:
    sum = inp
elif inp<=1000:
    sum = 99
    for i in range(100, inp+1):
        sum += check_han(change_list(i))

print(sum)