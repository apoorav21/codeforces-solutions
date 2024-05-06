n = int(input())
count = 0
prev = 0
for i in range(n):
    m = int(input())
    if m != prev:
        count +=1
    prev = m

print(count)