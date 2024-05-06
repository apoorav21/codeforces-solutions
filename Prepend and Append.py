for _ in range(int(input())):
    n = int(input())
    s = list(input())
    j = -1
    x = 0 
    if n%2 == 0:
        for i in range(n//2):
            if s[i] == s[j]:
                print(len(s[i:j])+1)
                x = 1
                break
            j -= 1
        if x == 0:
            print(0)
    else:
        for i in range(n//2):
            if s[i] == s[j]:
                print(len(s[i:j])+1)
                x = 1
                break
            j -= 1
        if x == 0:
            print(1)        