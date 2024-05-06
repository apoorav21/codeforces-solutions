def x():
    input()
    s = input()
    return str(s[s.index("1") : s.rindex("1")].count("0"))

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))