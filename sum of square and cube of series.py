print ('Enter the number n')
a=int(input())

print('Enter the number of the mathematical operation required') 
print ('')

print("""       1 - Sum of the numbers till n
        2 - sum of the squares of the numbers
	3 -sum of the cubes of the numbers """)


print('\n')
 
b=int(input())

if b>3:
  print('invalid entery')
elif b==1:
     p=a-1
     while(p>=0) :
       a=a+p
       p-=1
     print('sum of n termsis',a )
elif b==2 :

     p=a-1
     k=a**2
 
     while(p>=0) :

       k=k+p**2 
 
       p-=1
    
     print ('the sum of the square of the n numbers is ',k      )
elif b==3 :

     p=a-1
     k=a**3
 
     while(p>=0) :

       k=k+p**3
       p-=1
    
     print ('the sum of the cube of the n numbers is ',k )     







      
  
       
