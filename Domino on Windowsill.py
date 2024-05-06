def x():
    n, k ,k2 = map(int, input().split())
    w, b = map(int, input().split())
    x = min(k,k2) + abs(k-k2)//2
    y = min(n-k,n-k2) + abs((n-k) - (n-k2))//2
    if x>=w and y>=b:
        return "YES"
    return "NO"
           
t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))