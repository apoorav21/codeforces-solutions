n = int(input())
a = []
count = 0 
for i in range(n):
    s = input().split()
    a.append(s)

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][0] == a[j][1]:
            count += 1

print(count - n)