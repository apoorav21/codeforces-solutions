def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

def x(n):
    m = n
    s = 0
    while m > 0:
        s += m%10
        m = m//10
    res = gcd(n,s)
    if res > 1:
        return str(n)
    else:
        return x(n+1)

t = int(input())
a = []
for _ in range(t):
    n = int(input())
    a.append(x(n))
print("\n".join(a))