from pprint import pprint
n=int(input())
bis={}
qua={}
pri={}
cost=0
for i in range(0,n):
    bis[i]=input()
    qua[i]=int(input())
    pri[i]=int(input())
w=int(input())
corder={}
cstock={}
for i in range(0,w):
  corder[i]=input()
  cstock[i]=int(input())
for j in range(0,len(corder)):
    for i in range(0,len(bis)):
      print(234)  
      if bis[i]==corder[j]:
        print(23)
        if qua[i]>=cstock[i]:
             cost=cost+pri[i]*cstock[i]
             qua[i]=qua[i]-cstock[i]
             print(233)
        else:
            print('order cannot be placed')
            break
sol={}
for i in range(0,n):
    sol[bis[i]]=[qua[i],pri[i]]
print(cost)
pprint(sol)    
        






















































































































































