a=input()
sam=0
sa=0
su=0
b=set('!@#$%^&*()_+{}|?><.,')
if len(a)<8:
    print('Invalid')
    exit(0)
if a[0].isalpha():
    sam=1
for i in range(0,len(a)):
    if (a[i].isdigit()) :
        su=1
        break

for letter in a:
    if letter in b:
        sa=1
    
if sa==1 and sam==1 and su==1:
    print('Valid')
else:
    print('Invalid')
    
    
