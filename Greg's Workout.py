n = int(input())
s = [*map(int, input().split())]
b = c = bc = 0
for i in range(0,n,3):
    c += s[i]
for i in range(1,n,3):
    b += s[i]
for i in range(2,n,3):
    bc += s[i]
if b<bc and bc>c:
    print("back")
elif b>bc and b>c:
    print("biceps")
else:
    print("chest")