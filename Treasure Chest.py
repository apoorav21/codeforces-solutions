def x():
    x, y, k = map(int, input().split())
    if y <= x:
        print(max(x,y))
        return
    else:
        z = x + k
        if z >= y :
            print(y)
            return
        else:
            print(y + y-z)
            return
        
t = int(input())
for _ in range(t):
    x()