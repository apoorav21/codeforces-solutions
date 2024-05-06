for _ in range(int(input())):
  n,m = map(int,input().split())
  a=[]
  for i in range(n):
    a.append(input())
  a.sort()
  x=0
  sum=float("inf")
  for i in range(n):
    for j in range(i+1,n):
      if i!=j:
        for k in range(m):
          x += abs(ord(a[i][k])-ord(a[j][k]))
        sum = min(sum,x)
        x=0
  print(sum)