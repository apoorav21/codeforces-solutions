for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = []
    for i in sorted(set(a)):
        b.append(i)
        a.remove(i) 
    print(*(b+a))