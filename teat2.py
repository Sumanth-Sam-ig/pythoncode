n=int(input())
l={}
l[0]=input()
a=1
for i in range(1,n):
    t=input()
    for k in range(0,i):
        if k==i-1:
            l[a]=t
            a+=1
        if t!=l[k]:
            continue   
        else:
             break
for i in range(0,a):        
  print(l[i])
f=input()
for i in range(0,a):
    if f==l[i]:
        print('Found')
        break
