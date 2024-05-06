for i in range(5):
    m = input()
    for j in m:
        if j == '1':
            y = i
            a = 2 - y
            sum = abs(a)
            for k in m:
                if k == '0':
                    x = x+1
                if k == '1':
                    break
            b = 2 - x
            sum = sum + abs(b)
print(sum)
