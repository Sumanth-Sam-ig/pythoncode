print('Enter the values g')
g1=int(input('g1='))
g2=int(input('g2='))
g3=int(input('g3='))
g4=int(input('g4='))
g5=int(input('g5='))


print ('enter the value of n')
n=int(input())

if n%g1==0:
    print(g1,'is factor of n')
elif n%g2==0:
    print(g2,'is factor of n')

elif n%g3==0:
    print(g3,'is factor of n')
elif n%g4==0:
    print(g4,'is factor of n')
elif n%g5==0:
    print(g5,'is factor of n')

else :

    print ('n donot have factors in g')
