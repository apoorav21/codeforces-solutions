for _ in range(int(input())):
    input()
    s = input()
    for i in s:
        if i == "L":
            print("L",end="")
        if i == "R":
            print("R",end="")
        if i == "U":
            print("D",end="")
        if i == "D":
            print("U",end="")
    print()