for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    for i in range(n):
        if a[i] == "G":
            a[i] = 'B'
    for i in range(n):
        if b[i] == "G":
            b[i] = 'B'
    x = 0
    for i in range(n):
        if a[i] != b[i]:
            print("NO")
            x = 1
            break

    if x==0:
        print("YES")