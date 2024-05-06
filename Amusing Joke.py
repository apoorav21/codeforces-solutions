s = list(input())
a = list(input())
x = list(input())

y = s + a

if len(y) == len (x):
    for i in y:
        if i in x:
            x.remove(i)
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")