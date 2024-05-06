for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    even = []
    odd = []
    j = 0
    for i in s:
        if i%2 == 0 and j%2 != 0:
            odd.append(i)
        elif i%2 != 0 and j%2 == 0:
            even.append(i)
        j += 1
    if len(odd) != len(even):
        print(-1)
    else:
        print(len(odd))