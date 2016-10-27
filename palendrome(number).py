print('Enter the number of digits')
n=int(input())
a={}
print('Enter the digits one by one')
for i in range(0,n):
	a[i]=int(input())
p=0
q=n-1
while (p<=n and q>=0):
    if a[p]==a[q] :
            p+=1
            q-=1
            
    else :
            print('not a palendrome')
            break
if (p==n and q==-1): 
     print('it is a palendrome')

