def x():
    n, s = map(int, input().split())
    x = n + 1 - (n+1)//2
    return str(s//x)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))