n=int(input('Enter the number of digits '))
a=str(input('enter the number : '))

x={}
i=n-1
while True:
  x[i]=int(a[i])
  print(x[i])
  i-=1
  if i<0:
      break
    
q=int(a)    
b=n-1   
while True :
    if q%x[b]==0:
      print(x[b],'is a factor of n')
    b-=1
    if b<0 :
        break

