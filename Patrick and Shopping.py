a, b, c = map(int, input().split())
a,b = min(a,b),max(a,b)
sum = a
if c <= b+a:
    sum += c
    if b >= a+c:
        sum += a+c
    else:
        sum += b
else:
    sum += a+((b)*2)
print(sum)