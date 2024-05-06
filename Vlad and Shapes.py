def x():
    n = int(input())
    k = 0
    for i in range(n):
        a = input()
        if "010" in a:
            k = 1
    if k:
        print("TRIANGLE")
        return
    
    print("SQUARE")
    return
    
t = int(input())
for _ in range(t):
    x()