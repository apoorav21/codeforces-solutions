def x():
    n = int(input())
    a = [*map(int, input().split())]
    s = sum(a)
    if s%3 == 0:
        print(0)
        return
    else:
        if s%3 == 2:
            print(1)
            return
        elif s%3 == 1:
            for i in a:
                if i%3 == 1:
                    print(1)
                    return
                    break
            else:
                print(2)
                return
            
t = int(input())
for _ in range(t):
    x()