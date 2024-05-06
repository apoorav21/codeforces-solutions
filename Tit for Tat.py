def x():
    n, k = map(int, input().split())
    a = [*map(int, input().split())]
    for i in range(n-1):
        if a[i] != 0:
            if k > a[i]:
                k -= a[i]
                a[-1] += a[i]
                a[i] = 0
            else:
                a[i] -= k
                a[-1] += k
                break
    print(" ".join(map(str, a)))

t = int(input())
for _ in range(t):
    x()