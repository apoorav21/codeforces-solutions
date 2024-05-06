a = "codeforces"
for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != a[i]:
            count += 1
    print(count)