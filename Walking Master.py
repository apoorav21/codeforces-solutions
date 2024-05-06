def x():
    a, b, c, d = map(int, input().split())        
    if d >= b and d-b >= c-a :
        a += d -b
        return str(d-b + abs(a-c))
    else:
        return "-1"



t  = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))