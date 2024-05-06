for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    s = input()
    d = {}
    for i,j in enumerate(a):
        if j not in d:
            d.update({j:s[i]})
        else:
            if s[i] != d[j]:
                print("NO")
                break
    else:
        print("YES")