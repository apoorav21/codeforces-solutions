def x():
    n = int(input())
    a = [*map(int, input().split())]
    b = [0]*101
    for i in a:
        c = abs(i)
        if b[c] < 2:
            b[c] += 1
    if b[0] == 2:
        b[0] = 1
    return str(sum(b))


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))