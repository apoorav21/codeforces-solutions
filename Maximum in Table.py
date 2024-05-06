n = int(input())
if n==1:
    print(1)
else:
    a = [1]*n
    x = 1
    for i in range(1,n):
        for j in range(1,n):
            x += a[j]
            a[j] = x
        else:
            x = 1
    print(a[-1])