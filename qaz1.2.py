import math
n=int(input())
x={}
y={}
for i in range(1,n+1):
    x[i]=int(input())
    y[i]=int(input())
def dist(a,b,c,d):
    d=((a-c)**2+(b-d)**2)**(1/2)
    return d
min=100000
dis=[]
p=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
      c=dist(x[i],y[i],x[j],y[j])
      dis=dis+[c]
      if c<min:
          min=c
      p=p+[[i,j]]
ans=[]
k=3
for i in range(1,len(p)):
  if dis[i]==min:
    ans=ans+[(x[p[i][0]],y[p[i][0]])]
    ans=ans+[(x[p[i][1]],y[p[i][1]])]
q=set(ans)
w=list(q)
w.sort()
for i in range(0,len(w)):
    print(w[i])

