n=int(input())
x={}
y={}
d={}
di=[]
t=0
for i in range(0,n):
    x[i]=int(input())
    y[i]=int(input())
def dis(x1,y1,x2,y2):
    dist=0
    dist=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return dist
for i in range(0,n):
   x1=x[i]
   y1=y[i]
   for j in range(i+1,n):
       y2=y[j]
       x2=x[j]
       d[i,j]=dis(x1,y1,x2,y2)
       di=di+[d[i,j]]
di.sort()

for i in range(0,n):
   x1=x[i]
   y1=y[i]
   for j in range(i+1,n):
       y2=y[j]
       x2=x[j]
       d[i,j]=dis(x1,y1,x2,y2)
       if d[i,j]==di[0]:
           print((x1,y1))
           print((y1,y2))

