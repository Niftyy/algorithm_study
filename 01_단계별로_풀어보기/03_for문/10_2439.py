test_case = int(input())

for i in range(test_case):
    for j in range(test_case - i -1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print(" ",end="")
    print("")