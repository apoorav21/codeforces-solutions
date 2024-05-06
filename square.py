import math
for i in range(int(input())):

    x1 , y1 = map(int, input().split())
    x2 , y2 = map(int, input().split())
    x3 , y3 = map(int, input().split())
    x4 , y4 = map(int, input().split())
    a = []
    a.append(math.sqrt((x2-x1)**2 +(y2-y1)**2))
    a.append(math.sqrt((x3-x1)**2 +(y3-y1)**2))
    a.append(math.sqrt((x4-x1)**2 +(y4-y1)**2))
    print(math.ceil((max(a)**2))//2)
    