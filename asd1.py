print('Enter the word')
s=input()
n=len(s)
i=0
sam=0
while i<=n-1:
    j=1
    while j<=n-i-1:
        if  s[i]==s[-j]:
            sam=1
            break
        j+=1
    i+=1
if sam==0:
    print('Good')  
elif sam==1:
    print('Bad')
