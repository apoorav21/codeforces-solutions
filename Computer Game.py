def x():
    input()
    a = input()
    b = input()
    for i,j in zip(a,b):
        if i == j == "1":
            return "NO"
    else:
        return "YES"

t = int(input())
c = []
for _ in range(t):
    c.append(x())
print("\n".join(c))