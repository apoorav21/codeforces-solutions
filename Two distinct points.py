def x():
    l1, r1, l2, r2 = map(int, input().split())
    while l2 == l1:
        l2 += 1
    return " ".join(str(i) for i in [l1,l2])

t = int(input())
a =[]
for _ in range(t):
    a.append(x())
print("\n".join(a))