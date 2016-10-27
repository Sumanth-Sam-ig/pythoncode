import math
print('Enter the value of m')
m=int(input())
n=int(input('Enter the value of n'))
a=math.gcd(m,n)

if a==1:
    print('the numbers are co primes')
else :
    print('the numbers are not co prime')
