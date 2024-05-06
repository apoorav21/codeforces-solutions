for _ in range(int(input())):
    n = input()
    a = ["a","b","c","d","e","f","g","h"]
    a.remove(n[0])
    b = ['1','2','3','4','5','6','7','8']
    b.remove(n[1])
    for i in a:
        print(i,end='')
        print(n[1])
    for i in b:
        print(n[0],end='')
        print(i)