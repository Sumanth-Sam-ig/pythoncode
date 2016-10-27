n=int(input())
a={}
b=[]
for i in range(0,n):
    a[i]=int(input())
    b=b+[a[i]]
b.sort()
c=int(input("find"))
s=b
def fli(x):
      x.sort()
      y=len(x)
      print(y//2)
      global sam
      global s
      print(x[y//2])
      if c==x[y//2]:
          print('Found')
          sam=1
      elif c<x[y//2]:
        x=x[0:y//2]
        print(x,1)
        sam=0
      elif c>x[y//2]:
        x=x[y//2:(len(x)+1)]
        print(x,0)
        sam=0
      s=x
fli(b)
while True:
    fli(s)
    if sam==1:
        break
