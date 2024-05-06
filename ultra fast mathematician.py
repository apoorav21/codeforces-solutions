n = (input())
s = (input())
a = []
for i in range(len(s)):
    if s[i] == n[i]:
        a.append(0)
    else:
        a.append(1)

print(''.join(str(i) for i in a))
