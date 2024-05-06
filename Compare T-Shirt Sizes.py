for _ in range(int(input())):
    a, b = input().split()
    if a[-1] > b[-1]:
        print("<")
    elif a[-1] < b[-1]:
        print(">")
    else:
        if a.count("X") > b.count("X"):
            if a[-1] == "S":
                print("<")
            else:
                print(">")
        elif a.count("X") < b.count("X"):
            if a[-1] == "S":
                print(">")
            else:
                print("<")
        else:
            print("=")