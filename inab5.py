a=input().strip()
a=a.split()
a.sort()
for i in range(len(a)):
    print(a[i],a.count(a[i]))
