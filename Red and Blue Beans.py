for _ in range(int(input())):
    r, b, d = map(int, input().split())
    diff = abs(r-b)
    if diff <= d * min(r,b):
        print("yes")
    else:
        print("no")
