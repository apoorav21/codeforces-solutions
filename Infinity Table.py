for _ in range(int(input())):
    n=int(input())
    a=int((n-1)**0.5)  #index of the diagonal edge
    if n-a*a<=a+1:  #check whether it is closer to left edge of diagonal
        print(n-a*a,a+1)  
    else:
        print(a+1,(a+1)**2-n+1)