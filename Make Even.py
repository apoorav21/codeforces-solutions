for _ in range(int(input())):
    n = input()
    if int(n)%2 == 0:
        print(0)
    elif int(n[0])%2 == 0:
        print(1)
    else:
        for i in n:
            if int(i)%2 == 0:
                print(2)
                break
        else:
            print(-1) 