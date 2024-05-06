def x():
    n, q = map(int, input().split())
    a = [*map(int, input().split())]
    even = odd = sum = 0
    for i in a:
        if i%2 :
            odd += 1
        else:
            even += 1
        sum += i
    for i in range(q):
        x = input().split()
        if x[0] == "0":
            sum += int(x[1]) * even
            if int(x[1])%2 :
                odd += even
                even = 0
            b.append(sum)          
        else:
            sum += int(x[1]) * odd
            if int(x[1])%2 :
                even += odd
                odd = 0
            b.append(sum)        
    return

t = int(input())
b = []
for _ in range(t):
    x()
print("\n".join(str(i) for i in b))