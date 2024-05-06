for _ in range(int(input())):
    n = input()
    if n[-1] == "9":
        print(int(n)//10 + 1)
    else:
        print(int(n)//10)
        