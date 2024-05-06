s = input()
a = list(input().split())
x = 0
for i in range(len(a)):
    if a[i][0] == s[0] or a[i][1] == s[1]:
        print("YES")
        x = 1
        break
if x == 0:
    print("NO")