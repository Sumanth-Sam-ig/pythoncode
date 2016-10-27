rr=int(input())
rc=int(input())
qr=int(input())
qc=int(input())
a=[]
for x in range(1,9):
   for y in range(1,9):
       if (y+0*x==rr or x+0*y==rc) and (y+0*x==qr or x+0*y==qc):
           a=a+[(y,x)]
       elif (y+0*x==rr or x+0*y==rc) and (y-x==qr-qc or x+y==qr+qc) :
           a=a+[(y,x)]
a.sort()
for i in range(0,len(a)):
    print(a[i])
