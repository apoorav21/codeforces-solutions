def X():
    n = int(input()) - 1
    s = [*map(int, input().split())]
    a = sum(s)
    for i in s:
        if (a-i)/n == i:
            return "YES"
    return "NO"

t = int(input())
a = []
for _ in range(t):
    a.append(X())
print("\n".join(a)) 