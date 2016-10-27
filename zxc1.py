n=int(input())
x={}
y={}

for i in range (0,n):
    y[i]=int(input())
    x[i]=int(input())
for i in range(0,n):
  p=0
  gr=0
  while p<n:
    if gr<x[p]:
         gr=x[p]
         p+=1
        
    else:
         p+=1
  for a in range (0,n):
      if x[a]==gr:
          x[a]=0
          print(y[a])
          break
      
 
