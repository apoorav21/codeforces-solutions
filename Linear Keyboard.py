for _ in range(int(input())):
    a = input()
    b = input()
    count = 0
    prev = b[0]
    for i in b:
        count += abs(a.index(prev) - a.index(i))
        prev = i
    print(count)