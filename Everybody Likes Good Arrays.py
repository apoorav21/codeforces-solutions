def x():
    n = int(input())
    a = [*map(int, input().split())]
    c = 0
    for i in range(n-1):
        if a[i]%2 == a[i+1]%2:
            c+=1
    return str(c)

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))