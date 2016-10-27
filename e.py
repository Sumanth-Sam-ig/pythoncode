n=int(input())
a=[]
w=0
sam=0
for i in range(0,n):
    a=a+[int(input())]
a.sort()
x=int(input("find"))
def find(x):
         global w,sam,b,c
         if w==0:
            b=0
            c=len(a)-1
         mi=(c+b)//2
         if x==a[mi] or x==a[0] or x==a[len(a)-1]:
            print('found')
            sam=1
         elif x>a[mi]:
            c=len(a)-1
            b=mi
            w+=1
            if b==len(a)-2:
                print("not found")
            else:
                find(x)
         elif x<a[mi]:
             c=mi
             b=0
             w+=1
             if c==1:
                print("not found")
             else:
                find(x)
find(x) 
         
                   
         


