for _ in range(int(input())):
    input()
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    f = [*map(int, input().split())]
    if (a[0]==f[0]==b[0] or a[1]==f[1]==b[1]) and (a<f<b or b<f<a):
        res = abs(a[0]-b[0]) + abs(a[1]-b[1]) + 2
    else:
        res = abs(a[0]-b[0]) + abs(a[1]-b[1])
    print(res)