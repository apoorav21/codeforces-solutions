n = int(input())
if n%2:
    print(n//2)
    print( " ".join(["2"] * (n//2 - 1) + ["3"]))
else:
    print(n//2)
    print(' '.join(['2'] * n//2))