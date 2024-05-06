n, m = map(int, input().split())
count = 0
for i in range(1, n+1):
    if i%2 != 0:
        print("#"*m)
    else:
        if count == 0:
            print("."*(m-1) + "#")
            count = 1
        elif count == 1:
            print("#" + "."*(m-1))
            count = 0




