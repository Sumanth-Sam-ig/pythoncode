
while True :
 print('   Enter the borrowed day')                
 d=int(input())
 if d>31:
  print('invalid')
  continue
 print('   Enter the borrowed month') 
 m=int(input())
 print('   Enter the borrowed year') 
 y=int(input())

 if (d>31 or m>12 )  :
  print ('invalid entry,  try again')
  continue  
 else :
  if d==26:
    exp=1
  else :    
    exp=d+5
  if exp>=31 :
    exp-=31
  if (m==12 and d>=26) :
    y+=1
    if d>=26:
        m+=1
        m-=12
  break  
    
print()    
print ('expected return is on', exp,m,y) 
print ()
while True :
   print('Enter the returned day')
   d1=int(input())
   print('Enter the returned month')
   m1=int(input())
   print('Enter the returned year')
   y1=int(input())
   if (d1>31 or m1>12 or y1<y or(d1<d and m1==m)or(m1<m and y1==y))  :
    print ('invalid entry,  try again')
    continue
   else :
    if (d1<=exp and m1==m and y1==y) :
      print ('You reurned the book on time.  Fine  =  0' )
      break
      
    if (d1>exp and m1==m and y1==y) : 
      print("    the book is not returned on expected date  ")
      print()        
      fine=(d1-exp)*15
      print('your fine is',fine ,'rupees')
      break
     
    if (m1>m and y1==y):
      print("    the book is not returned on expected date  ")
      print()
      fine=(31+(d1-exp))*15+(m1-m)*500
      print('your fine is',fine ,'rupees')
      break
   
    if (y1>y):
      print("    the book is not returned on expected date  ")
      print() 
      fine=(31+(d1-exp))*15+(m1-m)*500+(y1-y)*10000
      print('your fine is',fine ,'rupees')
      break




