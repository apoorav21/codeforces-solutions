for _ in range(int(input())):
    a = []
    for i in range(8):
        s = input().split('.')
        s = set(input().split('.'))
        for i in s:
            if i != '':
                a.append(i)
    print(a)