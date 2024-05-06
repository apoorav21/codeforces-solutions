n = int(input())
for x in range(0,n):
    i = input()
    if len(i) > 10:
        print(i[0] + str((len(i)-2)) + i[-1])
    else:
        print(i)

