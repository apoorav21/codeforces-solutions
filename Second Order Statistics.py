def x():
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    if len(a) > 1:
        print(a[1])
        return
    print("NO")
    return
     
x()