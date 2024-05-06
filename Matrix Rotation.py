for _ in range(int(input())):
    a = input().split()
    b = input().split()
    c = set((max(a+b, key=int), min(a+b, key=int)))
    if c == set((a[0],b[1])) or c == set((a[1],b[0])):
        print("YES")
    else:
        print("NO")