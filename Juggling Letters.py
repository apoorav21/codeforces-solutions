for _ in range(int(input())):
    n = int(input())
    s =[]
    for i in range(n):
        s.append(input())
    a = ""
    for i in s:
        a+= i
    for i in a:
        if a.count(i)%n != 0:
            print("no")
            break
    else:
        print("yes")