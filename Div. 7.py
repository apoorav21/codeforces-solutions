for _ in range(int(input())):
    n = int(input())
    if n%7 == 0:
        print(n)
    else:
        if n%10 >= n%7:
            print(n-(n%7))
        else:
            print(n+(7-n%7))