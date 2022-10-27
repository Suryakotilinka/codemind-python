import math
n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
e=0
for i in a:
    b=math.sqrt(i)
    c.append(b)
for i in c:
    if i==int(i):
        d.append(i)
for i in d:
    e+=(i**2)
print(int(e))