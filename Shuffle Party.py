def x():
    n = bin(int(input()))
    return str((2**(len(n)-3)))

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))