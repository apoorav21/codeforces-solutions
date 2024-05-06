def x():
    n = int(input())
    s = input()
    r = ""
    a = "+"
    for i in s[:-1]:
        if i == "1":
            a = ["+", "-"][a == "+"]
        r += a
    return r


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))