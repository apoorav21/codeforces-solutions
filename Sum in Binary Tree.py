for _ in range(int(input())):
    n = int(input())
    sum = 0
    while n >= 1:
        sum += n
        n = n//2
    print(sum)