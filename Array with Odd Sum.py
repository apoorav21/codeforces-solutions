for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    odd = even = 0
    for i in s:
        if i%2 != 0:
            odd +=1
        else:
            even += 1
    if n % 2:
        if odd > 0:
            print("YES")
        else:
            print("NO")
    else:
        if odd > 0 and even > 0:
            print("YES")
        else:
            print("NO")