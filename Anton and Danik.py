n = int(input())
s = input()
a, d = 0, 0

for i in s:
    if i == "A":
        a += 1
    if i == "D":
        d += 1

if a > d:
    print("Anton")

if d > a:
    print("Danik")

else:
    print("Friendship")
