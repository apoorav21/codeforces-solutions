def x():
    n, l, r, k = map(int, input().split())
    a = [*map(int, input().split())]
    a = sorted(a)
    x = 0
    for i in a:
        if i > k:
            print(x)
            return
        else:
            if l <= i <= r:
                k -= i
                x += 1
    print(x)
    return

t = int(input())
for _ in range(t):
    x()