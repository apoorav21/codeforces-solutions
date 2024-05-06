for _ in range(int(input())):
    n = int(input())
    a = []
    if n%2 :
        a.append(3)
        a.append(1)
        a.append(2)
        for i in range(5,n+1,2):
            a.append(i)
            a.append(i-1)
        print(*a)
    else:
        for i in range(2,n+1,2):
            a.append(i)
            a.append(i-1)
        print(*a)