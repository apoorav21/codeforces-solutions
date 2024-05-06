def x():
    n = int(input()) + 1
    print(" ".join(str(n-x) for x in map(int, input().split())))
    return

t = int(input())
for _ in range(t):
    x()