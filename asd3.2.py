a=input()
n=len(a)
if  n==10:
    s={}
    for i in range(0,n):
        s[i]=a[i]    
    if int(s[0]+s[1])>12 or int(s[3]+s[4])>60 or int(s[6]+s[7])>60:
        print('Invalid')
    elif a[8]=="A":
        if s[0]=='1' and  s[1]=='2':
            s[1]=0
            s[0]=0
            for i in range(0,8):
                print(s[i],end='')
        else :
            print(a[0:8])
    else:
        d=str(int(s[0]+s[1])+12)
        
        if d=='24':
            s[0]=0
            s[1]=0
        else:
            if s[1]=='1' and s[2]=='2' :
              s[1]=d[1]
              s[0]=d[0]
        for i in range(0,8):
         print(s[i],end='')
