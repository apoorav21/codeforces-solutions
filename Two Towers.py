def x():
    n, m = map(int, input().split())
    a = input()
    a += input()[::-1]
    b = 0
    c = ""
    for i in a:
        if i == c:
            b += 1
        else:
            c = i
    if b > 1:
        print("NO")
        return
    print("YES")
    return

t = int(input())
for _ in range(t):
    x()