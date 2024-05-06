def x(): 
    n = int(input())
    a = input().split()
    c = a.count("-1")
    r = c*2 - n
    if r > 0:
        r = (r+1)//2
    else:
        r = 0
    if (c-r)%2:
        r += 1
    return str(r)

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a)) 