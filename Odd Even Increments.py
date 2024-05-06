for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    o = a[1::2]
    e = a[::2]
    parity1 = set([i%2 for i in o])
    parity2 = set([i%2 for i in e])

    if len(parity1) == 1 and len(parity2) == 1:
        print("YES")
    else:
        print("NO")