a=input()
sam=0
a=a.split()
b={}
for i in range(0,len(a)):
       for letter in a[i]:
           if letter in set('!?.,:;'):
               if letter==a[i][len(a[i])-1]:
                   print('good')
                   sam=0
               else:
                   print('bad')
                   sam=1
                   break
           else:
                sam=0
for i in range(0,len(a)):
    b[a[i]]=a.count(a[i])
if sam==0:
    print(b)

        
