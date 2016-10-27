print('consider the quadrtic equation of the form')
print('a*x**2+b*x+c')

print('enter the value of a ')
a=int(input())
print('enter the value of b ')
b=int(input())
print('enter the value of c ')
c=int(input())

d=b**2-4*a*c

if d<0 :
   print('roots are not possible')
else :
   x1=(-b+(d)**1/2 )/2*a
   x2=(-b-(d)**1/2 )/2*a
   print ('the roots of the equation are')
 
   print x1
   print x2