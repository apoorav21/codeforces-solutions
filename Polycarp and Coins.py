for _ in range(int(input())):
    n = int(input())
    c = n//3 + n%3%2
    print(c,(n-c)//2)