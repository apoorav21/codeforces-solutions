a = set(map(int, input().split()))
try:
    a.remove(0)
except:
    pass
print(len(a))