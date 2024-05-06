def x():
    n = int(input())
    s = input()
    a = 0
    b = 0
    for i in s:
        if i == "#" and b != 0:
            a += b
            b = 0
        elif i == ".":
            b += 1
            if b == 3:
                return "2"
    a += b
    return str(a)

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))