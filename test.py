s=input()
n=len(s)
s=s.upper()
sam=0
row=3
if (s.find('E') or s.find('E') or s.find('I') or s.find('O') )!=-1:
    row=1
    if s.find('A')!=-1:
        sam=1
        print('NO')
        exit(0)
elif s.find('A')!=-1:
    row=2
if row==3:
    for i in range(0,n):
        if s[i]=='Z' or 'X' or 'C'or 'V'or'B'or'M'or'N':
            print(45)
        else:
            sam=1
if row==2:
    for i in range(0,n):
         if s[i]==('A' or 'S' or 'D'or 'F'or'G'or'H'or'J'or'K'or'L')==s[]:
            print(34)
         else:
            sam=1

if sam==1:
    print(67)
