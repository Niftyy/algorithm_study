x = int(input())

total = 1
cnt = 1

while total < x:
  cnt+=1
  total+=cnt

ans = x-total+cnt
if cnt%2==0:
  print(f"{ans}/{cnt+1-ans}")
else:
  print(f"{cnt+1-ans}/{ans}")
