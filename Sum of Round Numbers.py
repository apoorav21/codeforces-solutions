for i in range(int(input())):
    n = input()
    a=[]
    j=1
    for i in n:
        a.append(int(int(i)*(10**(len(n)-j))))
        j +=1
        print(a)
    c = a.count(0)
    for k in range(c):
        a.remove(0)
        
    print(len(a))

    for i in a:
        print(i,end=" ")



