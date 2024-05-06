for _ in range(int(input())):
    n = int(input())
    a = 0
    for x in range(10):
        for y in range(10):
            if x + y >= n or x == y:
                continue
            z = n - x - y
            if z == x or z == y:
                continue
            elif x % 3 == 0 or y % 3 == 0 or z % 3 == 0:
                continue
            else:
                print("YES")
                print(x, y, z)
                a = 1
                break
        if a == 1:
            break        
    else:
        print("NO")