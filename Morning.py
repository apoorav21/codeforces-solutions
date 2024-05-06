def x():
    s = input()
    a = 1
    sum = 0
    for i in s:
        if int(i) == 0:
            i = 10
        if int(a) == 0:
            a = 10
        if int(i) > a:
            sum += int(i) - a
            sum += 1
        else:
            sum += a - int(i)
            sum += 1
        a = int(i)
    print(sum)
    return

t = int(input())
for _ in range(t):
    x()