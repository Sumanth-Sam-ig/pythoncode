n1=int(input())
x={}
for i in range(n1,-1,-1):
    a=int(input())
    x[i]=a
n2=int(input())
y={}
for i in range(n2,-1,-1):
    y[i]=int(input())
if n1>n2:
    for i in range(n1,n2,-1):
        y[i]=0
if n2>n1:
    for i in range(n2,n1,-1):
        x[i]=0
z=[]        
for i in range(n2+(n1//n2),-1,-1):
    z=z+[x[i]+y[i]]
print(z)    
    
    
    
        
 
