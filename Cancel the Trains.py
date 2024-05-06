def x():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    r = 0
    if m <= n:
        for i in a:
            if i in b:
                r += 1
    if m > n:
        for i in b:
            if i in a:
                r += 1
    return str(r)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))