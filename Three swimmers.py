def x():
    p, a, b, c = map(int, input().split())
    if p%a == 0 or p%b==0 or p%c == 0:
        return(str(0))
    if p <= a:
        a -= p
    else:
        a -= p%a
    if p <= b:
        b -= p
    else:
        b -= p%b
    if p <= c:
        c -= p
    else:
        c -= p%c
    
    return str(min(a,b,c)) 

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))