def x():
    n = int(input())
    x = [0,0]
    y = [0,0]
    for i in range(n):
        s = input().split()
        if s[0] == "0":
            s[1] = int(s[1])
            if s[1] > y[1]:
                y[1] = s[1]
            elif s[1] < y[0]:
                y[0] = s[1]
        else:
            s[0] = int(s[0])
            if s[0] > x[1]:
                x[1] = s[0]
            elif s[0] < x[0]:
                x[0] = s[0]
    r = 0
    for i in zip(x,y):
        r += abs(i[0]) + abs(i[1])
    return str(r*2)

t = int(input())
a= []
for _ in range(t):
    a.append(x())
print("\n".join(a))