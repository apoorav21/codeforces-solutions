for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    odd = even = 0
    for i in s:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd == n:
        print("YES")
    else:
        print("NO")