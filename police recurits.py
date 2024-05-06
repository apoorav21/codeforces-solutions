n = int(input())
e = map(int, input().split())
police = 0
count = 0
crime = 0
for i in e:
    police = police -  crime*(-1)
    if police < 0:
        police = 0
    crime =0
    if i < 0 :
        crime += i
    else:
        police += i
    if (crime)*(-1) > police:
        count += 1
print(count)