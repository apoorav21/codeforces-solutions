def x():
    s=input()
    tp=int(s[:2])
    c=str(tp%12)
    if len(c)==1:
        if c=='0':
            c='12'
        else:
            c='0'+c
    return  c+s[2:]+[' AM',' PM'][tp//12==1]   

t=int(input())
a=[]
for _ in range(t):
    a.append(x())
print('\n'.join(a))