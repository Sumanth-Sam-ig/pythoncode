a=input()
n=len(a)
p=[]
gr=0
for j in range(0,n):
    c=ord(a[j])
    for i in range(j+1,n):
       if ord(a[i])>=c+i-j or ord(a[i])==c+i-j-1:
            if i-j>=gr:
               gr=i-j
               c1=j
               c2=i
               h='stop'
       else:
          
           break
if h=='stop':             
   print(a[c1:c2+1])           
else:
    print('nothing in seqence')
