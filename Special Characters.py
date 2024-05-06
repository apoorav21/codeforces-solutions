def x():
    n = int(input())
    if n%2 :
        print("NO")
        return
    else:
        print("YES")
        print("AAB" * (n//2))
        return

t = int(input())
for _ in range(t):
    x()