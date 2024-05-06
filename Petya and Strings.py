a = input().lower()
b = input().lower()

for i in range(len(a)):
    if a[i] > b[i] :
        print('1')
        break
    elif b[i] > a[i]:
        print('-1')
        break
    elif a[i] == b[i]:
        print('0')
        break