n, q = map(int, input().split())
s = input()
x = [0]
for i in s:
    x.append(x[-1] + ord(i)-96)
for _ in range(q):
    a, b = map(int, input().split())
    print(x[b] - x[a-1])