a=[]
n1=int(input())
for i in range(n1,-1,-1):
    b=int(input())
    a=a+[b]
n2=int(input())
c=[]
for i in range(n2,-1,-1):
    b=int(input())
    c=c+[b]
if n1>n2:
    for i in range(0,n1-n2):
        c[0:0]=[0]
else:
    for i in range(0,n2-n1):
        a[0:0]=[0]
d=[]

for i in range(0,n2+(n1//n2)+1):
  d=d+[a[i]+c[i]]

print(d)


