for i in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    for s in a:
        print(s-b[n-1] if s!=b[n-1] else s-b[n-2],end=' ')