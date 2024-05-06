def x():
    s = input()
    a = set(s)
    if len(a) == 1:
        print(-1)
        return
    if len(a) == 2:
        for i in a:
            if s.count(i) == 3:
                print(6)
                return
        print(4)
        return
    print(4)
    return

t = int(input())
for _ in range(t):
    x()