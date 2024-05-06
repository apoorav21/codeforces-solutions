for _ in range(int(input())):
    s = input()
    two = 0
    one = 0
    for i in set(s):
        if s.count(i)>=2:
            two += 1
        else:
            one += 1
    print(two + one//2)