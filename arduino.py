#ARDUINO
'''
n=list(map(int,input().split()))
a=str(n)
c=0
for i in a:
    print(i)
    x=int(i)
    c+=x
print(c)

'''
a=list(map(int,input().split()))
mx=-1
s=0
for i in a:
    s=s+i
    if s>mx:
        mx=s
print(mx)


1 -2 3 4
6
