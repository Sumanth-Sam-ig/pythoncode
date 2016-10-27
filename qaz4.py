from pprint import pprint
a=input().strip().lower()
a=a.split()
b={}
for i in range(len(a)):
    if a[i][-1] in set('!?.,:;'):
        b[a[i][:-1]]=a.count(a[i])
    else:
        b[a[i]]=a.count(a[i])
    
pprint(b)
