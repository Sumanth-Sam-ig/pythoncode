print('enter the units')

units=int(input(''))

if (units<100) :
   bill=units*1
else:
   if units<200 :
      bill=100+(units-100)*1.5
   else :
      bill=100+(units-100)*3
print(bill)