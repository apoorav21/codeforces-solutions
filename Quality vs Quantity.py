def x():
    n = int(input())
    a = [*map(int, input().split())]
    a.sort()
    s = a[0]
    r = 0
    n = n//2 +1
    for i, j in zip(a[1:n], a[n:][::-1]):
        s += i
        r += j
        if s < r:
            return "YES"
    return "NO"

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))