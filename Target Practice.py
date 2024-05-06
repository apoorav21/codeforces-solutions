for _ in range(int(input())):
    sum = 0
    for i in range(10):
        n = input()
        for j in range(10):
            if n[j] == "X":
                sum += min(min(i, 9-i), min(j, 9-j)) + 1
    print(sum)