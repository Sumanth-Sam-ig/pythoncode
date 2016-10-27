rr=int(input())
rc=int(input())
qr=int(input())
qc=int(input())
rook=[]
queen=[]
sol=[]
for i in range(1,9):
      rook=rook+[(rr,i)]
for i in range(1,9):
    rook=rook+[(i,rc)]
for i in range(1,9):
      queen=queen+[(qr,i)]
for i in range(1,9):
    queen=queen+[(i,qc)]
for x in range(1,9):
    for y in range(1,9):
        if y-x==qc-qr:
            queen=queen+[(x,y)]
        if x+y==qr+qc:
            queen=queen+[(x,y)]
for i in range(0,len(queen)):
    for g in range(0,len(rook)):
        if queen[i]==rook[g]:
            sol=sol+[queen[i]]
print(queen)
print(rook)
sol=set(sol)
sol=list(sol)
print(sol)
           
    
