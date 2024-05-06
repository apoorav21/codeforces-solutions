for _ in range(int(input())):
    x = 0
    input()
    for i in range(8):
        n  = input()
        if "#.#" in n and x == 0:
            print(i+2, n.index("#")+2)
            x = 1