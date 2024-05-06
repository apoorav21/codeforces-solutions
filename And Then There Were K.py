for _ in range(int(input())):
    n = int(input())
    counter = 0
    while 2**counter <= n:
        counter += 1
 
    print(2 ** (counter - 1) - 1)