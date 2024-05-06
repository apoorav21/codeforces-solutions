n = int(input())
s = list(map(int, input().split()))
count = 0

while s[0] != max(s):
    Max = s.index(max(s))
    temp = s[Max]
    s[Max] = s[Max - 1]
    s[Max - 1] = temp
    count += 1

while s[-1] != min(s):
    Min = (n - 1) - (s[::-1].index(min(s)))
    temp = s[Min]
    s[Min] = s[Min + 1]
    s[Min + 1] = temp
    count += 1

print(count)
