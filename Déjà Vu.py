def x():
    s = input()
    l = len(s)
    if set(s) == {"a"}:
        return "NO"
    elif l%2 == 0:
        l //= 2
        if s[:l][::-1] == s[l + 1:] + "a"
            return f"YES\na{s}"
        return f"YES\n{s}a"
    else:
        l += 1
        l //= 2
        if s[:l][::-1] == s[l:] + "a":
            return f"YES\na{s}"
        return f"YES\n{s}a"

t = int(input())
a = []
for i in range(t):
    a.append(x())
print("\n".join(a))