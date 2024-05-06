def x():
    n = int(input())
    if n == 2:
        return "2"
    elif n%2:
        return "1"
    return "0"

t = int(input())
a = []
for i in range(t):
    a.append(x())
print("\n".join(a))