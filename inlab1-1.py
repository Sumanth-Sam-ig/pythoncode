import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
a=((x1-x2)**2+(y1-y2)**2)**0.5
d=a*(2)**(0.5)
print(format(d,'.2f'))
if x1==x2:
    w=(math.pi)/2
elif y1==y2:
    w=0
else:
      m=(y1-y2)/(x1-x2)
      s=-1/(m)
      w=math.atan(s)
x3=x1+a*math.sin(w)
x4=x2+a*math.sin(w)
y3=y1+a*math.cos(w)
y4=y2+a*math.cos(w)
print(int(x3),int(x4),int(y3),int(y4))



















