def x():
    a, b = map(int,input().split())
    if a%2 == b%2 == 0 or ((a%2 == 0 and a//2 != b) or (b%2 == 0 and b//2 != a)):
        return "YES"
    return "NO"

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))