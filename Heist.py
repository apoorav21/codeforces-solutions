n = int(input())
a =[*map(int, input().split())]
a = sorted(a)
count = 0
for i in range(n-1):
    count += a[i+1] - a[i] - 1
print(count)