def x():
    n, m = map(int, input().split())
    if n == m == 1:
        print(0)
        return
    else:
        x, y = max(n, m), min (n, m)
        print((2*(y-1))+x)
        return

t = int(input())
for _ in range(t):
    x()