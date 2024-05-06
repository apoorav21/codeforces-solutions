def x():
    input()
    b = input()
    q = 0
    for i in b:
        if i == "Q":
            q += 1
        else:
            q = max(0, q-1)
    if q == 0:
        return "Yes"
    else:
        return "No"
    
t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))