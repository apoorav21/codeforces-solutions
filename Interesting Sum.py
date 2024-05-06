def x():
    n = int(input())
    a = [*map(int, input().split())]
    a.sort()
    return str(sum(a[-2:]) - sum(a[:2]))
    
t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a)) 