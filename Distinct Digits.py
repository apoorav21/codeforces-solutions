a,b=map(int,input().split())
k=-1
for i in range(a,b+1):
    if(len(str(i))==len(set(str(i)))):
        k=i
print(k)