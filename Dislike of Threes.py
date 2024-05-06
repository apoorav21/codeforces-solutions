for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1,100000):
        if i%3 != 0 and i%10 != 3:
            count += 1
        if count == n:
            print(i)
            break