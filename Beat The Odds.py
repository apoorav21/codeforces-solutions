for _ in range(int(input())):
    n = int(input())
    s = [*map(int,input().split())]
    odd = 0
    for i in s:
        if i%2 :
            odd += 1
    print(min(n-odd,odd))    