n, x = map(int, input().split())
count = 0
for _ in range(n):
    s = input().split()
    if s[0] == '+':
        x += int(s[1])
    else:
        if int(s[1]) > x:
            count += 1
        else:
            x -= int(s[1])

print(x,count)