def x():
    n = input()
    for i in n:
        if i == "1":
            return "13"
        elif i == "3":
            return "31"


t = int(input())
a = []
for _ in range(t): 
    a.append(x())
print("\n".join(a))