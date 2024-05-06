for _ in range(int(int(input()))):
    n, k = map(int, input().split())
    s = input()
    if(k == 0 or s==s[::-1]):
        print(1)
    else:
        print(2)