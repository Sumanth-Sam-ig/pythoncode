m=int(input())
n=int(input())
if m>n:
    i=n
else:
    i=m
while i>1:
    if m%i==0:
        if n%i==0:
            print('Not coprime')
            break
        else:
            i=i-1
    else:
        i=i-1
else:
    print('Coprime')
