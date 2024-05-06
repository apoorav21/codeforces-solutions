for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    odd = even = 0
    for i in a:
        if i%2:
            odd += 1
        else:
            even += 1
    if odd == 0 or even == 0:
        print("YES")
    else:
        if min(a)%2:
            print("YES")
        else:
            print("NO")