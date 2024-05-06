n = int(input())
p1 = set(input().split()[1:])
p2 = set(input().split()[1:])

count = 0
for i in range(1, n + 1):
    if str(i) in p1 or str(i) in p2:
        count += 1

if count == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
