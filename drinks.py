n = int(input())
s = input().split()
sum = 0
for i in s:
    sum += int(i)
result = sum / n
result = "{:.12f}".format(result)
print(result)