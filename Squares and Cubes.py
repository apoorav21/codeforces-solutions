for _ in range(int(input())):
    n = int(input())
    a = set()
    for i in range(1,n+1):
        if i**2 <= n:
            a.add(i**2)
        else:
            break
    for i in range(1,n+1):
        if i**3 <= n:
            a.add(i**3)
        else:
            break
    print(len(a))