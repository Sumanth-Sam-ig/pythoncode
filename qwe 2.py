print ('Enter the life span in days')
n=float(input())
if (n>40 or n<0):
    print ('invalid')
else :
    lifespan=n*86400.00000
    print('life span =',lifespan,'seconds')
