for _ in range(int(input())):
    n = int(input())
    enemy = input().strip()
    gregor = input().strip()
    count = 0
    visited = set()
    for i in range(n):
        if gregor[i] == "1":
            if enemy[i] == "0":
                count += 1
            elif i > 0 and enemy[i-1] == "1" and i-1 not in visited:
                count += 1
                visited.add(i-1)
            elif i < n-1 and enemy[i+1] == "1" and i+1 not in visited:
                count += 1
                visited.add(i+1)
    print(count)