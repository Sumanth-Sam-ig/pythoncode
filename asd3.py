a=input()
n=len(a)
if n==8:
    s={}
    for i in range(0,n):
        s[i]=a[i]    
    if int(s[0]+s[1])>23 or int(s[3]+s[4])>60 or int(s[6]+s[7])>60:
        print('Invalid')
    elif int(s[0]+s[1])>12:
        d=str(int(s[0]+s[1])-12)
        if len(d)==1:
        
         s[1]=d[0]
         s[0]=0
        if len(d)==2:
           s[1]=d[1]
           s[0]=d[0]    
        
        s[8]='P'
        s[9]='M'
        for i in range(0,n+2):
         print(s[i],end='')
    else :
        s[8]='A'
        s[9]='M'
        for i in range(0,n+2):
         print(s[i],end='')
if  n==10:
    s={}
    for i in range(0,n):
        s[i]=a[i]    
    if int(s[0]+s[1])>12 or int(s[3]+s[4])>60 or int(s[6]+s[7])>60:
        print('Invalid')
    elif a[8]=="A":
        print(a[0:8])
    else:
        d=str(int(s[0]+s[1])+12)
        s[1]=d[1]
        s[0]=d[0]
        for i in range(0,8):
         print(s[i],end='')
    
