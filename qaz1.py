n=int(input())
x={}
y={}
lan=0
d={}
t=0
mx={}
my={}
for i in range(0,n):
    x[i]=int(input())
    y[i]=int(input())
def dis(x1,y1,x2,y2):
    dist=0
    dist=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return dist
mi=10000
for i in range(0,n):
   x1=x[i]
   y1=y[i]
   for j in range(i+1,n):
       y2=y[j]
       x2=x[j]
       d[i,j]=dis(x1,y1,x2,y2)
       if d[i,j]<mi:
           mi=d[i,j]
           mx1=x[i]
           my1=y[i]
           mx2=x[j]
           my2=y[j]
           lan=0
      
print((mx1,my1))
print((my1,my2))
if lan==1:
    for i in range(0,t):
        print((mx[i],my[i]))
        print((my[i+1],my[i+1]))


