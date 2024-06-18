#BORING ARRAYS
'''
1 index 
INPUT
4
1 2 3 4.....1st - last =3 and 2-3 =1 total 1+3=4
OUTPUT
4

2 4 6 8.......4+2=6

1 2 3 4 5



n=int(input())
a=list(map(int,input().split()))
d=0
a.sort()
x=n//2
for i in range(0,(n//2)):
    d+=a[n-1]-a[i]
    n=n-1
print(d)



4 
1 2 3 4
4




n=int(input())
a=list(map(int,input().split()))
a.sort()
d=0
f=0
n=n-1
while f<=n:
    d+=a[n]-a[f]
    n=n-1
    f+=1
print(d)
    

'''






'''

5
1 2 3 4 5
14
'''

n1=int(input())
n2=int(input())
a=list(map(int,input().split()))
a.sort()
l=[]
s=0
mx=0
for i in a:
    l.append(i)




'''
for i in range(1,n2):
    s+=(a[n1]*n2+a[n1-1]*i)
    l.append(s)
    n1-=n1
    if mx<s:
        mx=s
print(l)
print(mx)




while n1!=0:
    s+=(a[n1]*i+1+a[n1-1]*i)
    print(s)
    l.append(s)
    n1-=n1
if mx<s:
    mx=s
print(l)
print(mx)
'''























