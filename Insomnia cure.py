k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
a = []
for i in range(d):
    a.append(0)

for i in range(k-1,d,k):
    a[i] = 1

for i in range(l-1,d,l):
    a[i] = 1

for i in range(m-1,d,m):
    a[i] = 1

for i in range(n-1,d,n):
    a[i] = 1

print(a.count(1))
