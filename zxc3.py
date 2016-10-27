z=0
e={}
r=int(input())
c=int(input())
if r<0 or c<0 :
    print('invalid')
for j in range(1,c+1):
    for i in range(1,r+1):
        e[i,j]=int(input())
        if e[i,j]==0:
             z=z+1
if z>=(c*r)/2:
    print('Sparse')
else:
    print('Not Sparse')
    
