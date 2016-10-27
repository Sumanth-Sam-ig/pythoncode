n=int(input())
a={}
b=int(input('enter the floor'))
while True:
 for i in range(0,n+1):
    if i==b:
        a[i]='(lift)'
    else:
        a[i]='(    )'
 for i in range(n,-1,-1):
    print('[  ',i,'  ]','-----',a[i])  
 b-=1
 for i in range(4000000):
     samq=1
     if i<5:
         print(' ')
 if b<0:
     break
 
