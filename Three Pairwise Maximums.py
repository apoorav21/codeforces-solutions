for _ in range(int(input())):
    xyz = [*map(int, input().split())]
    xyz.sort()
    if xyz[2] == xyz[1]:
        print("YES")
        if xyz[2] == xyz[0]:
            print(xyz[2], xyz[2], 1)
        else:
            print(xyz[2], xyz[0], 1)
    else:
        print("NO")
