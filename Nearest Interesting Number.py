s = input()
a = 0
for i in s:
    a += int(i)

while a%4 != 0:
    s = str(int(s) + 1)
    a = 0
    for i in s:
        a += int(i)
print(s)