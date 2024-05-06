n = int(input())
if n % 2:
    print(-1)
else:
    temp = [0] * n
    for x in range(n // 2):
        temp[x] = str(n - x)  
        temp[n - 1 - x] = str(x + 1)
    print(*temp)