for _ in range(int(input())):
    n = int(input())
    a = input().split()
    sum = 0
    for i in a:
            sum += abs(int(i))
    print(sum)