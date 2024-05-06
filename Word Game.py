for i in range(int(input())):
    n = int(input())
    a, b, c = set(input().split()), set(input().split()), set(input().split())
    uniq = (a.difference(b.union(c))
            .union(b.difference(a.union(c)))
            .union(c.difference(a.union(b))))
    repeat = (a.intersection(b).difference(c)
              .union(b.intersection(c).difference(a)
                     .union(c.intersection(a).difference(b))))
    res = [0,0,0]
    for i, v in enumerate([a,b,c]):
        for j in v:
            if j in uniq:
                res[i] += 3
            elif j in repeat:
                res[i] += 1
    print(*res)