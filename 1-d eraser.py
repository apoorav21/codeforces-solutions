for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    count = i = 0
    while i< n:
        if s[i] == "B":
            i += k
            count += 1
        else:       
            i+=1
    print(count)