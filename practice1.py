a={}
for i in range(0,9):
    a[i]=int(input())
for i in range(0,3):
    if a[i]==a[i+3]==a[i+6]:
        print(1)
    
