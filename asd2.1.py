a=input()
a=a.upper()
q=0
w=0
e=0
for letter in a:
    if letter in set('QWERTYUIOP'):
           q+=1
    if letter in set('ASDFGHJKL')  :
           w+=1
    if letter in set('ZXCVBNM'):
           e+=1
if q==len(a) or w==len(a) or e==len(a):
       print("Good")
else:
    print('Bad')
