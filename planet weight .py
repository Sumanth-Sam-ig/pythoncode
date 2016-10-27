print('Enter your weight on Earth')

a=float(input())

mass=a/9.798

Ju	=24.92
Ne	=11.15
Sa	=10.44
Ea	=9.798
Ur	=8.87
Ve	=8.87
Ma	=3.71
Me	=3.7
Mo	=1.62
Pl	=0.58
 
print('Enter the planet number you want to find your weight')

print("""             2  Jupiter	
             3	Neptune	
             4	Saturn	
             5	Earth	
             6	Uranus	
             7	Venus	
             8	Mars	
             9	Mercury	
            10	Moon	 
            11	Pluto	""")

b=int(input())

if b==2 :
   w=mass*Ju
   print 'your weight on jupiter is',w
elif b==3 :
   w=mass*Ne 
   print 'your weight on neptune is',w
elif b==4 :
   w=mass*Sa
   print 'your weight on saturn is',w   

elif b==5 :
   w=mass*Ea
   print 'your weight on earth is',w

elif b==6 :
   w=mass*Ur
   print 'your weight on uranus is',w

elif b==7 :
   w=mass*Ve 
   print 'your weight on venus is',w

elif b==8 :
   w=mass*Ma
   print 'your weight on mars is',w

elif b==9 :
   w=mass*Me
   print 'your weight on mercury is',w

elif b==10 :
   w=mass*Mo
   print 'your weight on moon is',w

elif b==11 :
   w=mass*Pl
   print 'your weight on pluto is',w 
else :
   print('invalid entry')

print('as per nasa values')