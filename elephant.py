x = int(input())
# 1 2 3 4 5
count = 0
if x >= 5:
    count +=1*(x//5)
    x = x%5
if x >= 4:
    count +=1*(x//4)
    x = x%4
if x >= 3:
    count +=1*(x//3)
    x = x%3
if x >= 2:
    count +=1*(x//2)
    x = x%2

print(count + x)