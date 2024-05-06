for _ in range(int(input())):
    n = int(input())
    a = []
    if n%2 != 0:
        for i in range(1,n+1):
            if i != (n//2) +1:
                a.append(i)
        a.reverse()
        a.append((n//2)+1)
    else:
        for i in range(1,n+1):
            a.append(i)
        a.reverse()
    print(*a)