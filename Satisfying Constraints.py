t = int(input())

for i in range(t):
    more = float('-inf')
    less = float('inf')
    equal = []
    n = int(input())
    for j in range(n):
        k, x = map(int, input().split())
        if k == 1:
            more = max(more,x)
        elif k == 2:
            less = min(less, x)
        elif k == 3:
            equal.append(x)

    result = ((less - more)+1) 

    for j in equal:
            if more <= j <= less:
                result -= 1
    
    print(max(0,result))