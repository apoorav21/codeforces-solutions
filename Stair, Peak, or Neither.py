def x():
    a, b, c = map(int, input().split())
    if a<b<c:
        return "STAIR"
    elif a<b>c:
        return "PEAK"
    return "NONE"

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))