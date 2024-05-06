for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    sum1 = 0
    for i in s:
        if i%2 == 0:
            sum1 += i
    if sum1 > sum(s)-sum1 :
        print("YES")
    else:
        print("NO")