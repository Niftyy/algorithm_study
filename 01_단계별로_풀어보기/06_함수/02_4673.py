def d(n):
    sum = n
    while True:
        sum += n % 10
        n = n // 10
        if n == 0:
            break
    return sum
lia = []
lib = []
for i in range(1,10001):
    lia.append(i)
    lib.append(d(i))
for i in sorted(list(set(lia)-set(lib))):
    print(i)