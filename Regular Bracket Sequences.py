def x():
    n = int(input())
    a, b, c = "()", "(", ")"
    r = []
    for i in range(n):
        r.append(f"{i*b}{(n-i) * a}{i*c}\n")
    print("".join(r),end ="")

t = int(input())
for _ in range(t):
    x()