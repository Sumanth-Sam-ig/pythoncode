s=input()
n=len(s)
s=s.upper()
sam=0
row=3
if (s.find('E') or s.find('U') or s.find('I') or s.find('O') )!=-1:
    row=1
    if s.find('A')!=-1:
        sam=1
        print('NO')
        exit(0)
elif s.find('A')!=-1:
    row=2
if row==3:
    count=0
    row3 = set("zxcvbnm")
    for letter in s:
       if letter in row3:
          count+=1        
if row==2:   
    count=0
    row2= set("ASDFGHJKL")
    for letter in s:
       if letter in row2:
          count+=1    
if row==1:    
    count=0
    row1= set("QWERTYUIOP")
    for letter in s:
        if letter in row1:
            count+=1   
if count!=n:
    print('NO')
else:
    print('YES')
    
