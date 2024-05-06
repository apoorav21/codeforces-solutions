testcases = int(input())
for _ in range(testcases):
    s = input()
    count_a = 0
    count_b = 0
    for i in range(len(s)):
        if s[i] == "A":
            count_a += 1
        elif s[i] == "B":
            count_b += 1
    if count_a > count_b:
        print("A")
    else:
        print("B")