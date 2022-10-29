s=input()
c=0
mx=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U': 
        c+=1
    elif i==' ':
        if c>mx:
            mx=c
        c=0
        
if mx>c:
    print(mx) 
else:
    print(c)
        