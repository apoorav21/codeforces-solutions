for _ in range(int(input())):
    a, b, k = map(int,input().split())
    sum = 0
    if k%2:
        sum += (a-b)*(k//2)
        sum += a
    else:
        sum += (a-b)*(k//2)
    print(sum)