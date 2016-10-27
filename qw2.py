a=str(input())
n=len(a)
x={}
i=n-1
while True:
  x[i]=int(a[i])
  
  i-=1
  if i<0:
      break
    
q=int(a)    
b=n-1   
while b>=0 :
    if q%x[b]==0:
      print(x[b])
      b-=1
      continue
    
    elif(b==0):
        print('No factors')
        b-=1
    else:
        b-=1
        
