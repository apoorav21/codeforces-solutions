n, k = map(int, input().split())
s = list(map(int, input().split()))

for i in s:
    if 5-i < k:
        s.remove(i)


print(len(s)//3)