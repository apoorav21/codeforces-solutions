def x():
    n = int(input())
    print(" ".join(str(2 * i) for i in range(1, n+1)))


t = int(input())
for _ in range(t):
    x()