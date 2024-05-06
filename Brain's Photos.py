n, m = map(int, input().split())
a = []
for i in range(n):
    s = input().split()
    a.append(s)
b = ['C', 'M', 'Y']
x=0
for i in b:
    if i in a:
        print("Color")
        x = 1
if x == 0:
    print("#Black&White")