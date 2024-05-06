n, h= map(int, input().split())
a = input().split()
count = 0
for i in a:
    if int(i) > h:
        count += 2
    else:
        count += 1

print(count)