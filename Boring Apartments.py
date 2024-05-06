for _ in range(int(input())):
    n = input()
    k = len(n)+1
    print(10*(int(n[0]) - 1) + k*(k-1)//2)
