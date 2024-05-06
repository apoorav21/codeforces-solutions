for _ in range(int(input())):
    s = input()
    if s.count('A') + s.count('C') == s.count('B'):
        print("YES")
    else:
        print("NO")