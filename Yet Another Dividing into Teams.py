def x():
    n = int(input())
    a = [*map(int, input().split())]
    for i in a:
        if i+1 in a:
            return "2"
    return "1"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))