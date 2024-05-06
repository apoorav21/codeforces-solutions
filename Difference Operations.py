def x():
    n = int(input())
    a = [*map(int, input().split())]
    b = a[0]
    for i in a[1:]:
        if i%b != 0:
            return "NO"
    return "YES"

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))