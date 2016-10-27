print('Enter the number')
p=int(input())
if p<0:
  print('fibonacci series not possible')

a=0
b=1
while (a<=p) :
  print a
  c=a+b
  a=b 
  b=c

print('series is completed')
   