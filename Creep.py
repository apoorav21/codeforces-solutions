def x():
    a, b = map(int, input().split())
    if a < b:
        s = "01" * a + "1" * (b - a)
    else:
        s = "01" * b + "0" * (a - b)
    return

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))