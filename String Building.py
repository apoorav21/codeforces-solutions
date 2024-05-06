def X():
    s = input()
    a = s.split("b")
    b = s.split("a")
    if "a" in a or "b" in b:
        return "NO"
    return "YES"

t = int(input())
a = []
for _ in range(t):
    a.append(X())
print("\n".join(a))