n, m = map(int, input().split())
x = y = 0
r = [*range(1,n+1)]
q = set()
for i in range(n):
    a, b = map(int, input().split()) 
    for i in range(a,b+1):
        q.add(i)
for i in q:
    try:
        r.remove(i)
    except:
        pass
print(len(r))
print(*r)