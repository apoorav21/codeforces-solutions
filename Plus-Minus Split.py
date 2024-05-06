for _ in range(int(input())):
    input()
    s = input()
    print(max(s.count("-"), s.count("+"))-min(s.count("-"),s.count("+")))