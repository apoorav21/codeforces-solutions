def x():
    n = int(input())
    a = "##"
    b = ".."
    q = p = 0
    for i in range(n):
        r = ""
        if p == 0:
            q = 0
            p +=1
        else:
            q = 1
            p -=1    
        for j in range(n):
            if q == 0:   
                r += a
                q += 1
            else:
                r += b
                q -= 1
        print(r)
        print(r)

t = int(input())
for _ in range(t):
    x() 