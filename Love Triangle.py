n = int(input())
a = [*map(int, input().split())]
for i in range(n//2 + 1):
    if a[a[a[i]-1]-1] == i+1:
        print("YES")
        break
else:
    print("NO")