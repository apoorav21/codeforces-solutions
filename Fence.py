def x():
    s = sum(map(int, input().split())) - 1
    return str(s)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))