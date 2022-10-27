n=int(input())
d=(n//2)+1
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n//2):
    b.append(a[i])
for i in range(n):
    if a[i] not in b:
        c.append(a[i])
c.reverse()
e=c+b
print(*e)