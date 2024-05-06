for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    count = 0
    for i in s:
        if i not in a:
            a.append(i)
            count +=2
        else:
            count +=1
    print(count)