n = int(input())
s = list(map(int, input().split()))
a = b = 0
for i in range(n):
    if i%2 == 0:
        a += max(s[0],s[-1])
        s.remove(max(s[0],s[-1]))
    else:
        b += max(s[0],s[-1])
        s.remove(max(s[0],s[-1]))
    
print(a,b)