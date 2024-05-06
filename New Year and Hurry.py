n , k = map(int, input().split())
total = 240 - k
sum = 0
count = 1
if total == 0 or total < 0:
    print(0)
    
else:
    for i in range(n+1):
        sum += 5*i
        if sum > total:
            print(i-1)
            count = 0
            break
        elif sum == total:
            print(i)
            count = 0
            break
    if count != 0:
        print(n)