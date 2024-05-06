for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    for i,j in zip(s, sorted(s)):      #zip combines elemets of both into a tuple
        if (i+j)%2:               # if sum is odd means both have diff parity
            print("NO")
            break
    else:
        print("YES")