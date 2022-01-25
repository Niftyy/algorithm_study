hour, minute = map(int,input().split())

if minute>=45:
    print(hour%24, minute-45)
else:
    print((hour-1)%24, 60+minute-45)