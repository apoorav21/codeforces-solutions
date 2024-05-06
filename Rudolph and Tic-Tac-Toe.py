# sometimes if else is all you need :)
t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = input()
    if a[0] == b[0] and b[0] == c[0] and a[0] != ".":
        print(a[0])
    elif a[1] == b[1] and b[1] == c[1] and a[1] != ".":
        print(a[1])
    elif a[2] == b[2] and b[2] == c[2] and a[2] != ".":
        print(a[2])
    elif a[0] == a[1] and a[1] == a[2] and a[0] != ".":
        print(a[0])
    elif b[0] == b[1] and b[1] == b[2] and b[0] != ".":
        print(b[0])
    elif c[0] == c[1] and c[1] == c[2] and c[0] != ".":
        print(c[0])
    elif a[0] == b[1] and b[1] == c[2] and a[0] != ".":
        print(a[0])
    elif a[2] == b[1] and b[1] == c[0] and a[2] != ".":
        print(a[2])
    else:
        print("DRAW")