for _ in range(int(input())):
    n = int(input())
    s = set(input())
    a = ["T",'i','m','u','r']
    x = 0
    if len(a) == len(s):
        for i in a:
            if i not in s:
                print("NO")
                x = 1
                break
        if x == 0:
            print("YES")
    else:
        print("NO")