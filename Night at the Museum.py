c = 97
count = 0
for i in map(ord,input()):
	x = abs(c-i)
	count += min(x,26-x)
	c = i
print(count)