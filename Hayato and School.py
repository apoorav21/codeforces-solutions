def x():
    n = int(input())
    a = [*map(int, input().split())]
    e = []
    o = []
    for i in range(n):
        if a[i]%2 :
            o.append(i+1)
        else:
            e.append(i+1)
    if len(o) >= 3:
        return "YES\n" + str(o[0]) +" "+ str(o[1]) +" "+ str(o[2])
    elif len(o) >= 1 and len(e) >= 2:
        return "YES\n" + str(o[0]) +" "+  str(e[0]) +" "+  str(e[1])
    else:
        return "NO"           

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))