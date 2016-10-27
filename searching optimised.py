n=int(input())
a=[]
w=0
sam=0
for i in range(0,n):
    a=a+[int(input())]
e=int(input('find'))
def find(x):
    global sam,w
    if w==0:
        b=0
        c=len(a)-1
    mi=(c+b)//2
    if x==a[mi] or x==a[0] or x==a[len(a)-1]:
        sam=1
        print('found')
    elif x>a[mi]:
        b=mi
        c=len(a)-1
        w+=1
        if b==len(a)-2:
            sam=0
        else:
            find(x)
    elif x<a[mi]:
        b=0
        w+=1
        c=mi
        if c==1:
            sam=0
        else:
            find(x)
find(e)
if sam==0:
    print('not found')
    
    
    
