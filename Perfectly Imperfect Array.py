import math as m
for _ in range(1, int(input()) + 1):
    input()
    a = list(map(int, input().split()))
    f = 0
    for i in a:
        if (m.sqrt(i).is_integer() == False):
            f = 1      
    if f == 1:
        print("YES")
    else:
        print("NO")