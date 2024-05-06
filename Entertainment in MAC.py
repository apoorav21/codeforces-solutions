def x():
    n = int(input())
    s = input()
    if s[::-1] < s:
        print(s[::-1],end="")
        print(s)
        return
    print(s)
    return

t = int(input())
for _ in range(t):
    x()