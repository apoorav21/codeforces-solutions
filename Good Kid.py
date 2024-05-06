for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    s[s.index(min(s))] +=1
    count = 0
    for i in s:
        count *= i
    print(count)