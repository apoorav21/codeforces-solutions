m = c = 0
for _ in range(int(input())):
    s = input()
    if s[2] > s[0]:
        c +=1
    elif s[0] > s[2]:
        m += 1
    
if m == c:
    print("Friendship is magic!^^")
elif m > c:
    print("Mishka")
else:
    print("Chris")

    