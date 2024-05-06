n = int(input())
s = input()
res = 0
count = 0
for i in s:
    if i == "x":
        if count < 2:
            count += 1
        else:
            res += 1
    else:
        count = 0
print(res)