s = input()
a = s.count("a")
if a > (len(s)+1)//2:
    print(len(s))
else:
    print(2*a -1)