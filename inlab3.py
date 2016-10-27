import math
n=int(input())
a={}
b={}
for i in range(1,n+1):
    a[i]=int(input())
for i in range(2,n+1):
    b[a[i]]=math.gcd(a[1],a[i])
c=list(b.items())
c.sort()
for i in range(0,n):
    print(b.get(c[i]))


















    
