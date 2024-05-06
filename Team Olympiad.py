n = int(input())
s = list(map(int, input().split()))
t = min(s.count(1),s.count(2),s.count(3))
a1 = []
a2 = []
a3 = []

for i in range(n):
    if s[i] == 1:
        a1.append(i+1)
    if s[i] == 2:
        a2.append(i+1)
    if s[i] == 3:
        a3.append(i+1)

print(t)
for i in range(t):
    print(a1[i],a2[i],a3[i])