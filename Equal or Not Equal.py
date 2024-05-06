def x():
    s = input()
    if s.count("N") == 1:
        return "NO"
    return "YES"


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))