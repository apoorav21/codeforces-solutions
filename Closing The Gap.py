def x():
    n = int(input())
    a = [*map(int, input().split())]
    if sum(a)%n == 0:
        return "0"
    return "1"
 
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))