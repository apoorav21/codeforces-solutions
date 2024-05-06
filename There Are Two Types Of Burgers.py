def i():
    j, *k = map(int, input().split())
    j //= 2
    s = list(map(int, input().split()))
    ii = 0 if s[0] > s[1] else 1
    tp = min(j, k[ii])
    j -= tp
    c = s[ii] * tp
    tp = min(j, k[ii - 1])
    j -= tp
    c += s[ii - 1] * tp
    return str(c)
 
t = int(input())
a = []
for _ in range(t):
    a.append(i())
print("\n".join(a))
