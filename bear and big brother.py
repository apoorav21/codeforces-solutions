a, b = map(int, input())
count = 0
while True:
    a = a*3
    b = b*2
    count += 1
    if a > b:
        print(count)