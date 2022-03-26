target = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
for i in target:
    s = s.replace(i, "a")
print(len(s))