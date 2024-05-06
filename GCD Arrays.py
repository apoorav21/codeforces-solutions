def x():
    l, r, k = map(int, input().split())
    if l == r:
        if l == 1:
            print("NO")
            return
        print("YES")
        return
    a = (r - l + 1)//2
    if l%2 and (r-l+1)%2:
        a += 1
    if a <= k:
        print("YES")
        return
    print("NO")
    return

t = int(input())
for _ in range(t):
    x()