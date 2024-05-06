s = input()
n = s.split('+')

for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            temp = n[j+1]
            n[j+1] = n[j]
            n[j] = temp

x=[]

if len(n) > 1:
    for i in range(len(n)):
        x.append(n[i]) 
        x.append('+')

    if x[-1] == '+':
        x.pop()

    print(''.join(str(i) for i in x))

else:
    print(''.join(str(i) for i in n))