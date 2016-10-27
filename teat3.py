from pprint import pprint
a=input().lower()
g=set(a)
b=[]
d={}
e={}
l=[0,0,0,0,0]
for letter in a:
    b=b+[letter]

for letter in g:
    d[letter]=b.count(letter)
    if l[b.count(letter)]==0:
        l[b.count(letter)]=[letter]
    else:
         l[b.count(letter)]=l[b.count(letter)]+[letter]
    e[b.count(letter)]=l[b.count(letter)]

    
pprint(d)
pprint(e)
