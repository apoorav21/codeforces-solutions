def x():
    n = int(input())
    if n%3 == 0:
        print("21" * (n//3))
    elif n%3 == 2:
        print("21" * (n//3), end = "")
        print("2")
    else:
        print("1", end = "")
        print("21" * (n//3))
    return

t = int(input())
for _ in range(t):
    x()