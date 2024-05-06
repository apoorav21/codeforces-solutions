def x():
    n = int(input())
    s = input()
    if len(set(s)) == 2:
        if s[0] == "L":
            print(s.index("R"))
            return
        print(0)
        return
    print(-1)
    return


t = int(input())
for _ in range(t):
    x()