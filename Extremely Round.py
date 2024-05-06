def x():
    n = input()
    x = len(n)
    if int(n) <= 10:
        print(n)
        return
    else:
        print(9*(x-1) + int(n[0]))
        return

t = int(input())
for _ in range(t):
    x()