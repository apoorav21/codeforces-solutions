def x():
    input()
    a = list(map(int, input().split()))
    b = -1
    n = 0
    for i in a:
        if b < i:
            b = i
            n += 1
        elif b == i:
            n += 1
            b = i+1
            
    return str(n)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))