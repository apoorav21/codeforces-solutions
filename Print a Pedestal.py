for _ in range(int(input())):
    n = int(input())
    min = (n - 3) // 3
    if n % 3 == 1:
        print(min + 1, min + 3, min)
    elif n % 3 == 2:
        print(min + 2, min + 3, min)
    else:
        print(min + 1, min + 2, min)