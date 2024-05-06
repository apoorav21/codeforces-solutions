n = int(input())
count = 0
denomination = [100,20,10,5,1]

for i in denomination:
    count += n// i
    n %= i

print(count) 