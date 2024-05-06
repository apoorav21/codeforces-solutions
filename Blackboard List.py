def x():
    n = int(input())
    a = [*map(int, input().split())]
    max = min = 0
    for i in a:
        if i > max:
            max = i
        elif i < min:
            min = i 
    if min < 0:
        return str(min)
    return str(max)       

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))