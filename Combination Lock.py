n = int(input())
s = input()
e = input()
sum = 0
for i in range(n):
    if s[i] != e[i]:
        sum += min(min(abs(int(s[i]) - int(e[i])) , 1 + abs(9-int(s[i])+(int(e[i])))), 1 + abs(9+(int(s[i])-(int(e[i])))))
    print(sum)
print(sum)