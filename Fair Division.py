for i in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    x = s.count(1)
    y = s.count(2)
    if x%2 == 0 :
        if y%2 == 0:
            print("YES")
        else:
            if x>=2:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")