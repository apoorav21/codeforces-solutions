n = int(input())
count = 0
for i in range(n):
    w = input()
    list = w.split()
    x = 0
    for j in list:
        if int(j) == 1:
            x = x + 1
    if x > 1:
        count = count + 1
print(count)

