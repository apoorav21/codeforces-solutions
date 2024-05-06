for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b:
        print("First")
    elif b > a:
        print("Second")
    elif a == b:
        if c%2 :
            print("Second")
        else:
            print("Frist")