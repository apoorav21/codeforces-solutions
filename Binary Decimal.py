def x():
    s = input()
    return str(max(s))

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))