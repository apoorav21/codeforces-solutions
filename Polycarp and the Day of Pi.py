a= "3141592653589793238462643383279"
for _ in range(int(input())):
    n = input()
    count = 0
    for i in range(len(n)):
        if n[i] == a[i]:
            count += 1
        else:
            break
    print(count)