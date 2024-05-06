def x():
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    m +=1
    s = ["B"]*m
    for i in a:
        if i > m - i :
            i = -i
        if s[i] != "A":
            s[i] = "A"
        elif s[-i] != "A":
            s[-i] = "A"
    
    return "".join(s[1:])

t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))