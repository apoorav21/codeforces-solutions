n = int(input())
a = 0
for i in range(1,n):
    a += i
    n -= a
    if n == 0:
        print(i)
        break 
    else:
        print(i-1)
        break
