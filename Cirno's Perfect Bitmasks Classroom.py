def x():
    n = bin(int(input()))[2:]
    if n.count("1") == 1:
        if n == "1":
            return "3"
        c = n[:-1] + "1"
        return str(int(c, 2))
    else:
        c = n[n.rindex("1") :]
        return str(int(c, 2))
   
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))