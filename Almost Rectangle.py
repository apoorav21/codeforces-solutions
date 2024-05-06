for i in range(int(input())):
	n=int(input())
	x,a,b=[],[],[]
	for j in range(n):
		s=list(input())
		x.append(s)
		t=s[:]
		if "*" in t:
			for k in range(n):
				if t[k]=="*":
					r=t.index("*")
					t[r]="."
					if r in b:
						b=[r-1,r-1]
					else:
						b.append(r)
					if j in a:
						a=[j-1,j-1]
					else:
						a.append(j)
	x[a[0]][b[1]],x[a[1]][b[0]]="*","*"
	for j in range(n):
		print("".join(x[j]))