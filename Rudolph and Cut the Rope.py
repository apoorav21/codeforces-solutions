for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a>b:
            count +=1
    print(count)