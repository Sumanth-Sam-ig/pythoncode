a=input()
b={}
if a[8]=='A':
    if a[0]==1 and a[1]==2:
        b[0]=0
        b[1]=0
        print(b[0],end='')
        print(b[1],end='')
        print(a[2:8])
     else:   
    print(a[:8])
elif a[0]=='1'and a[1]=='2':
    a[0]='0'
    a[1]='0'
    print(a[:8])
else:    
    b[0]=int(a[0])+1
    b[1]=int(a[1])+2
    print(b[0],end='')
    print(b[1],end='')
    print(a[2:8])    
    
    
