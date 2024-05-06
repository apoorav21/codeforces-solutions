def x():
    n = int(input())
    a = list(map(int, input().split()))
    s = 1
    for i in a:
        s *= i
    s += n-1        
    return str(s*2022)

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))