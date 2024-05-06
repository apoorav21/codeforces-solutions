def X():
    n = int(input())
    s = input()
    res = 0
    for i in range(n):
        if s[i] == "A":
            p = 0
            for j in s[i+1:]:
                if j == "A":
                    break
                p += 1
            res = max(res, p)
    return str(res)

t = int(input())
a = []
for _ in range(t):
    a.append(X())
print("\n".join(a)) 