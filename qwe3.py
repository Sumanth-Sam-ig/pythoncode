m=int(input('Enter the values of m  :  '))
n=int(input('Enter the values of n  :  '))

def gcd (a,b):
   if a>b :
     while True :
      c=a%b
      if a%b==1:
        return 1
        break
      if c==0 :
        return b
        break
      else :
        a=b
        b=c
    
    
   if a<b  :  
        while True :
     
         c=b%a
        
         if c==0:
            return a
            break
         if c==1:
            return 1
            break
         elif c!=0:
            b=a
            a=c
        
     

g=gcd(m,n)
if g==1:
   print('they are co primes')
else :
   print('they are not co primes')
