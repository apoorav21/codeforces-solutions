n = int(input())

while True:
    count = 0
    n +=1
    x = list(str(n))
    for i in str(n):
        if x.count(i) < 2:
            count += 1
    if count == len(x):
        print(n)
        break

