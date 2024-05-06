n = input().split()
a = []
for i in n:
    if i not in a:
        a.append(i)
print(len(n) - len(a))
