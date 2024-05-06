for _ in range(int(input())):
    n = int(input())
    s = [*input().split()]
    a = set(s)
    count = 0
    for i in reversed(s):
        try:
            a.remove(i)
            count += 1
        except:
            break
    if count == 0:
        print(n-1)
    else:
        print(n-count)
            