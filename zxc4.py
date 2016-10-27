d=int(input())
x={}
y={}
a={}
b=list()
for i in range(d,0,-1):
    x[i]=int(input())
d1=int(input())
for i in range(d1,0,-1):
    y[i]=int(input())
for i in range(1,d+(d1%d)+1):
    if d==d1:
        a[i]=x[i]+y[i]
    else:
        for i in range(1,d):
            a[i]=x[i]+y[i]
            
for i in range(d,0,-1):
    b[0:0]=[a[d]]
print(b)
