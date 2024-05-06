for i in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    count = remove = add = 0
    for i in range(n):
        if s[i] != f[i]:
            if f[i] == '0':
                remove +=1
            else:
                add +=1
    print(min(remove,add) + abs(remove-add))
                 

