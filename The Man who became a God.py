def x():
    n, k = map(int, input().split())
    n, k -= 1
    s = [*map(int, input().split())]
    b = []
    for i in range(n):
        b.append(abs(s[i] - s[i+1]))
    b.sort()
    return str(sum(b[ :len(b) - k]))


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))