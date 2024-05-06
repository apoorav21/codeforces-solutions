r, c = map(int, input().split())
a = []
for _ in range(r):
    s = input()
    a.append(s)
b = []
for i in a:
    if "S" in i:
        b.append(1)
d = []
for i in zip(*a):
    if "S" in i:
        d.append(1)
print(r*c-len(b)*len(d))