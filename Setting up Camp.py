def x():
    a, b, c = map(int, input().split())
    a += b // 3
    m = b % 3
    c += m
    if m and c < 3:
        return "-1"
    a += (c - 1) // 3 + 1
    return str(a)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))