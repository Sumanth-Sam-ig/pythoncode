a={}
i=0
l={}
gr=0

while True:
    a[i]=input()
    
    l[i]=len(a[i])
    
    if l[i]>gr:
        gr=l[i]
        n=a[i]
    if a[i]=='Stop':
        print(i+1)
        break
    i+=1
print(n)
print(gr) 
    
