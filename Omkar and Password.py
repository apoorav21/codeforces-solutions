def X():
    n = int(input())
    a = set(map(int, input().split()))
    if len(a) > 1:
        return "1"
    return str(n)

t = int(input())
a = []
for _ in range(t):
    a.append(X())
print("\n".join(a))