n, k = map(int, input().split())

for i in range(k):
    if n > 0:
        if n%10 != 0:
            n -= 1
        else:
            n = n//10

print(n)