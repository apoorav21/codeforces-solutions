n = int(input())
s = list(map(int,input().split()))
x = [s[0]]
count = 0
for i in s[1:]:
    if i < min(x):
        count+=1
    if i > max(x):
        count+=1
    x.append(i)



print(count)