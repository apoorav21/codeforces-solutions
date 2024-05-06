n, t = map(int, input().split())
s = input()
y = list(s)
x = list(s)

for i in range(t):
    for j in range(len(s)-1):
        if y[j] == 'B' and y[j+1] == 'G':
            temp = x[j+1]
            x[j+1] = x[j]
            x[j] = temp
           
    s = ''.join(str(i) for i in x)
    y = list(s)

print(''.join(str(i) for i in y))
