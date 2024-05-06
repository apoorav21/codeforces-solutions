for _ in range(int(input())):
    n = int(input())
    res = ""
    for i in range(9,0,-1):
        if n <= i:
            res = str(n) + res
            break
        else:
            n -= i
            res = str(i) + res
    print(res)