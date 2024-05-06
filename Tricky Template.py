for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()
    #checks if all characters of c are in a and b
    if all(k in [i,j] for i, j, k in zip(a,b,c)):   
        print("NO")                                 
    else:
        print("YES")