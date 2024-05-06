n = int(input())
for i in range(n):
    w = input()
    x = 0
    for j in w:
        if j == '+': 
            x += 1
        if j == '-':
            x -= 1

print(x)


    