n = int(input())

s = input().split()
x =[]
for i in range(1, n+1):
    x.append(s.index(str(i))+1)
y=[]
for i in x:
    y.append(i)
    y.append(' ')

if y[-1] == ' ':
    y.pop()

print(''.join(str(i) for i in y))
