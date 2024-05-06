def x():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 < l2 or l1 > r2 :
        return str(l1+l2)
    return str(max(l1,l2))
    
t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))