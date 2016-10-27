print('enter the number')
n=int(input())
if (n<=0 or n==1) :
    print('in valid input')
else :
    i=2
    while i<n :
            if n%i==0 :
                print ('n is not a prime number')
                break
            else :
                i+=1
                
    if i==n :
         print ('number is a prime nuber')
        
