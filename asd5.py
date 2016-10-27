a=input()
d=int(input())
for i in range(0,len(a)):
    c=ord(a[i])
    c+=d
    print(chr(c),end='')
