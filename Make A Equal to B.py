def x():
    input()
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    c = d =0
    for i,j in zip(a,b):
        if i == 1 and j == 0:
            c += 1
            d += 1
        elif i == 0 and j == 1:
            c -= 1
            d += 1
    if abs(c) == d:
        return str(abs(c))
    else:
        return str(abs(c) + 1)
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))