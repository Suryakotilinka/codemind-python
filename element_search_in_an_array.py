n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l:
    if k in l:
        print('True')
        break
    else:
        print('False')
        break