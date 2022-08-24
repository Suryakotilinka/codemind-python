
n=int(input())
x=n*n
s=0
while x>0:
    z=x%10
    s+=z
    x=x//10
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')
    
        
