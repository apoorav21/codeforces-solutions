for _ in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))
    
    if len(a) <= (max(a) - min(a)):
        print("YES")
    else:
        print("NO")