a = []
x = 0
n = int(input())
for i in range(n):
    a.append(input())
for i in range(n):
    s = a[i].split("|")
    if s[0][0] == s[0][1] == "O":
        s[0] = "++|"
        a[i] = s[0]+s[1]
        x = 1
        print("YES")
        break
    elif s[1][0] == s[1][1] == "O":
        s[1] = "|++"
        a[i] = s[0]+s[1]
        x = 1
        print("YES")
        break
    
if x == 0:
    print("NO")
else:
    for i in range(n):
        print(a[i])
