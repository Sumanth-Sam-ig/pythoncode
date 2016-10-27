print('enter the year')
a=int(input())
 
if a%400==0 :
   print a,'is aleap year'
elif a%100==0 :
   print  a,'is not leap year'
elif a%4==0 :
   print a,'is aleap year'
else : 
   print a,'is not a leap year'