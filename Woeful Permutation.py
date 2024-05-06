def x():
    n = int(input())
    b = []
    if n%2 :
        b.append(1)
        for i in range(2,n):
            b.append(i+1)
            b.append(i)
    else:
        for i in range(1,n):
            b.append(i+1)
            b.append(i)
    print(" ".join(str(i) for i in b))

t = int(input())
for _ in range(t):
    x()