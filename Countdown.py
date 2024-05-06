def x():
    n = int(input())
    s = input()
    p = int(s)
    r = 0
    if s[-1] != "0":
        r -= 1
    r += n - s.count("0")
    s = int(s)    
    while s > 0:
        r += s%10
        s //= 10
    return str(r)
t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))