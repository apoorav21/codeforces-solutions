for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a==b and c%2 == 0)or (b==c and a%2 == 0)or (a==c and b%2 == 0):
            print("YES")
    else:
        if a== b+c or b == a+c or c == b+a:
            print("YES")
        else:
            print("NO")