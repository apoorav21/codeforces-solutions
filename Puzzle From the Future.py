def x():
    n = int(input())
    b = input()
    r = ""
    a = -1
    for i in b:
        if (a == 2 and i == "1") or (a == 1 and i == "0"):
            r += "0"
            a = int(i)
        else:
            r += "1"
            a = int(i) + 1
    return r 

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))