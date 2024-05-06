for _ in range(int(input())):
    s = input()
    key = []
    for i in s:
        if i in "rgb":
            key.append(i)
        elif i in "RGB":
            if i.lower() not in key:
                print("NO")
                break
    else:
        print("YES")