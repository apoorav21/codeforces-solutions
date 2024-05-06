for _ in range(int(input())):
    s = input()
    count = 0
    count += (ord(s[0])-97) * 25
    if s[0] < s[1]:
        count += ord(s[1])-97
    else:
        count += ord(s[1]) -96
    print(count)