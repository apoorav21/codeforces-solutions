s = input()
counter = 0
q = []
a = []
for i, v in enumerate(s):
    if v == "Q":
        q.append(i)
    elif v == "A":
        a.append(i)
 
temp = [m for x in q for z in a for m in q if z > x and m > z]
print(len(temp))