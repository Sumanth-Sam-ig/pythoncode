import sys
n=int(input('Enter the number of floors'))
b=int(input('Iitial floor of lift'))
if b>n:
    print("Invalid")
    sys.exit()
up=[]
do=[]
p={}
print("""IEnter the button """)
for i in range(0,2*n+2):
    qwe=input()
    if qwe=='':
        break
    if  int(qwe)>n or int(qwe)==b or int(qwe)<-n:
        print("wrong inputs")
        break
    if i==0:
        fi=int(qwe)
        se=0
    if i==1:
        se=int(qwe)
    if len(qwe)==1:
        up=up+[int(qwe)]
    else:
        do=do+[int(qwe[1:])]
    if qwe=='':
        break
print(up,do)   
if b<fi:
    sam=1
elif b==fi:
    if b<se:
        sam=1
    else :
        sam=2
else:
    sam=2
print(fi,se,sam)
s=list(set(up)|set(do))
s.sort()
print(s)
ld=[]
lu=[]



for i in range (len(s)):
        if s[i]<b:
            ld=ld+[s[i]]
        if s[i]>b:
            lu=lu+[s[i]]
cyc=0
print(lu,ld)
if sam==1:
    z=2
elif sam==2:
    z=3
if sam==2 and len(lu)==0:
    z=1

for q in range(0,z):
 a={}
 while True:
  wait=0
  for i in range(n+1):
    p[i]='   '
  for i in range(0,n+1):
     if i==b:
         a[i]='(l f )'
     else:
         a[i]='(    )'
  if b in ld and sam==2 and cyc==0:
         p[b]='p   d'
         wait=1
  elif b in lu and sam==1 and cyc==0:
         p[b]='p  k'
         wait=1
  if b==max(s):
      p[max(s)]='  p   k'
  for i in range(n,-1,-1):
         print('[  ',i,'  ]','-----',a[i],'   ','  ',p[i])
  if sam==1:
     b+=1
  if sam==2:
      b-=1      
  for i in range(3000000):
      samq=1
      if i<5:
          if i==3 and wait==1:
              print('p  p   k')
          print(' ')
    
  for i in range(3000000):
      samq=1       
  if (b<0 or b>=max(s)) and sam==1:
      sam=2
      
      break
  if (b<0 or b>=max(s)) and sam==2:
      sam=1
      cyc=1
      break 



































