n = int(input())
a = []
if n == 1:
    print("I hate it")

else:
    for i in range(n):
        if i%2 == 0:
            a.append("I hate that")
        else:
            a.append("I love that")
    if n%2 == 0:
        a[-1] = 'I love it'
    else:
        a[-1] = "I hate it"
    l = []
    if len(a) > 1:
        for i in a:
            l.append(i)
            l.append(' ')
    else:
        l = a
    print(''.join(str(i) for i in l))