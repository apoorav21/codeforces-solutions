for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(1,2*n,2):
        a.append(i)
    print(*a)