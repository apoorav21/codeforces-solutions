n, k = map(int, input().split())
a = [*map(int, input().split())]
if len(set(a)) < k:
    print("NO")
else:
    print("YES")
    b = []
    for i in set(a):
        if len(b) != k:
            b.append(a.index(i)+1)
        else:
            break
    print(*b)