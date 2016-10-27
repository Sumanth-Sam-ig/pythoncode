print("Enter the number")

p=int(input())

if p<0:
 
   print(' factorial not possible')


if (p==0 or p==1) :

   print ('p!=1')

elif p>0:    

   fact=1
  
   l=1
   
   while(l<=p):
  
     fact=fact*l
  
     l=l+1

   print('factorial of the number is:',fact)
