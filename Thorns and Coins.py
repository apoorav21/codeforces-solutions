def x():
    n = int(input())
    a = input()
    if "**" in a:
        print(a[:a.index("**")].count("@"))
        return
    print(a.count("@"))
    return


t = int(input())
for _ in range(t):
    x()