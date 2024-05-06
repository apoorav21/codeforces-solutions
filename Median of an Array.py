def x():
    n = int(input())
    a = [*map(int, input().split())]
    a.sort()
    b = (n+1)//2 - 1
    p = a[b]
    q = 0
    for i in a[b::]:
        if p == i:
            q += 1
        else:
            break
    return str(q)

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))