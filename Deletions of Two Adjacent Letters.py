for _ in range(int(input())):
    s = input()
    a = input()
    x = []
    for i,j in enumerate(s):
        if j == a:
            x.append(i)
    for i in x:
        if i%2 ==0 :
            print("YES")
            break
    else:
        print("NO")