n = int(input())
s = input()
a = 0
res = []
for i in range(n):
    a += i
    try:
        res.append(s[a])
    except:
        break
print(''.join(str(i) for i in res))