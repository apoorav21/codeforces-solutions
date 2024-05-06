for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    counter = [0] * (n + 1)
 
    for x in a:
        if counter[x] < 2:
            counter[x] += 1
        elif counter[x] < 3:  
            print(x)
            break
    else:
        print(-1)