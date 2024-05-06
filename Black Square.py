a, b, c, d = map(int, input().split())
s = input()
y=[]
for i in s:
    y.append(int(i))
x = (int(a*int(y.count(1))) + int(b*int(y.count(2))) + int(c*int(y.count(3))) + int(d*int(y.count(4))))
print(x)