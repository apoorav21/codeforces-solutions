for _ in range(int(input())):
    n = int(input())
    b = 0
    if n%3 > 0:
        b = 1
    if n == 1:
        b = 2
    elif n == 2:
        b = 1
    print(b+(n//3))