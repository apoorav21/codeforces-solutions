for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    odd = even = 0
    for i in s:
        if s%2 !=0 :
            odd += 1
    if odd%2 == 0:
        print("YES")
    else:
        print("NO")