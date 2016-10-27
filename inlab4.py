n=3
b={}
a={}
c=[]
for i in range(0,n):
    q=int(input())
    w=int(input())
    e=int(input())
    a[i]=q+w+e
    b[i]=a[i]
    c=c+[a[i]]
c.sort()
print(c)

