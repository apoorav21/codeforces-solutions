s = input()
upper, lower = 0,0
for i in s:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

if upper > lower:
    print(s.upper())

else:
    print(s.lower())
