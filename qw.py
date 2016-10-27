n=int(input('Enter the number of places : '))
l={}
ml={}
for i in range(0,n):
    print ('data for place',i+1)
    l[i]=int(input('enter water in liter from this place  : ' ))
    ml[i]=int(input('enter water in milli liter from this place : '))

liter=0.00
milli=0.00
for i in range (0,n) :
    
    liter=liter+l[i]
    milli=milli+ml[i]
total=liter+(milli)*0.001
print ('the total water in the dam is ',total,'liters')
    
