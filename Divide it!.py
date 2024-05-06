def x():
    n = int(input())
    r = 0
    while n > 0:
        if n == 1:
            return str(r)
        if n%5 == 0:
            n = (4*n)//5
        elif n%3 == 0:
            n = (2*n)//3 
        elif n%2 == 0:
            n //= 2
        else:
            return "-1"
        r += 1
        


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))