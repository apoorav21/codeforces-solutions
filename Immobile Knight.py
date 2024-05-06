def x():
    a, b = map(int, input().split())
    if a > 3 or b > 3:
        return "1 1"
    elif a == 1 or b == 1:
        return "1 1"
    else:
        return "2 2"
    

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))