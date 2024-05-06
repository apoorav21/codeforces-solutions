a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
sum = 0
if f > e:
    sum += min(b,c,d) * f
    x = min(b,c,d)
    d -= x
    sum += min(a,d) * e
else:
    sum += min(a,d) * e
    x = min(a,d)
    d -= x
    sum += min(b,c,d) * f
print(sum)