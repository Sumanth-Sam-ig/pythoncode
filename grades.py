print('Enter marks in subject 1')
a=int(input())
print('Enter marks in subject 2')
b=int(input())
print('Enter marks in subject 3')
c=int(input())
print('Enter marks in subject 4')
d=int(input())

if (a>100 or b>100 or c>100 or d>100) :
   print('invalid entry') 

avg=(a+b+c+d)/4

if avg>=90 :
  print('your performance is out standing')
elif avg>=85 :
  print('your performance is good ')
elif avg>=75 :
  print('your performance is average,need to improve')
elif avg<=75 :
  print('fail')  