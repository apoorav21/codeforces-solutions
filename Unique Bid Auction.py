from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = [*map(int, input().split())]
    a = defaultdict(int)
    b = set()
    
    for i,j in enumerate(s):
        a[j] += 1
        if a[j] == 1:
            b.add(j)
        elif j in b:
            b.remove(j)
        
    if len(b) == 0:
        print(-1)
    else:
        print(s.index(min(b))+1)