x,y,z=map(int,input().split())
cl=x*((1+y/100)**z)
ci="{:.2f}".format(cl)
print(ci)