def x():
    s = input()
    a = s[0]
    for i in s[1:]:
        if i == "0":
            a += i
        else:
            break
    b = s[len(a):]
    if not b:
        return "-1"
    elif a == b or int(a) >= int(b):
        return "-1"
    else:
        return  a + " " + b


t = int(input())
a = []
for _ in range(t):
    a.append(x())
print("\n".join(a))