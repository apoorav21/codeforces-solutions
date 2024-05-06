a=[6,10,14]
for _ in range(int(input())):
	n=int(input())
	if n<=30:
		print("NO")
	elif n-30 in a:
		print("YES")
		print(6,10,15,n-31)
	else:
		print("YES")
		print(6,10,14,n-30)