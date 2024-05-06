for _ in range(int(input())):
    s = list(input())
    n = len(s)
    for i in range(n,0,-1):
        if chr(i+96) == s[0]:
            s.pop(0)
        elif chr(i+96) == s[-1]:
            s.pop()   
        else:
            break
    if len(s) > 0:
        print("NO")
    else:
        print("YES")