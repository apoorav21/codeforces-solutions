for _ in range(int(input())):
    n, m, k, h = map(int, input().split())
    s = [*map(int, input().split())]
    count = 0
    for i in s:
        if abs(h-i) <= (m-1)*k and i != h:
            if abs(h-i)%k == 0:
                count += 1
    print(count)