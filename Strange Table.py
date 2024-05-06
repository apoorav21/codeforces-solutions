for _ in range(int(input())):
    n, m, x = map(int, input().split())
    x -= 1
    print(x%n*m+x//n+1)