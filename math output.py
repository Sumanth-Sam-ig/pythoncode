print('enter the variables')
x=int(input('x:'))
y=int(input('y:'))



print ("""    1   addition
        2   subraction
        3   multiplication
        4   division """)
print ()


while True :
   a=int(input('enter the output required   :  '))

   if a==1:
    r=x+y
    print (r)
    break
   elif a==2:
    r=x-y
    print (r)
    break
    
   elif a==3:
    r=x*y
    print (r)
    break
   elif a==4:
    r=x/y
    print (r)
    break
   else  :
    print('invalid entry')
