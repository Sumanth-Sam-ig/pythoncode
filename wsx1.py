from collections import OrderedDict
n=int(input())
a=OrderedDict()
keys={}
for i in range(0,n):
    a[i]=input()
for i in range(0,n):
    b=[]
    for j in range(0,len(a[i])):
        if a[i][j]==a[i][::-1][j]:
            if j<len(a[i])//2:
               b=b+[j]
               keys[a[i]]=b

c=list(keys.keys())
sam=0
for i in range(0,len(c)):
    for j in range(0,len(c)):
        if (keys[c[i]]==keys[c[j]]) and (i!=j):
            print(c[i])
            sam=1
            break
if sam==0:
    print('Not isomorphoc')
    


















