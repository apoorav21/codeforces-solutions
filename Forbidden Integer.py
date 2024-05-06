def x():
    n, k , x = map(int, input().split())
    a = [i for i in range(1,4) if i != x]
    b = n//a[0]
    if n % a[0] == 0 and a[0] <= k:
        print("YES")
        print(b)
        print(" ".join(map(str, [a[0]] * b)))
        return   
    elif a[1] <= k:
        print("YES")
        print(b)
        b -= 1
        print(" ".join(map(str, [a[1], *[a[0]] * b])))
        return
    else:
        print("NO")
        return
    return
t = int(input())
for _ in range(t):
    x()