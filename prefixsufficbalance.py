#PREFIX SUFFIX BALANCE
'''
INPUT
5
1 2 3 4 5
OUTPUT
[13,9,3,5,15]



n=int(input())
l=[]
s=0
a=list(map(int,input().split()))
for i in range(0,n-1):
    s+=a[i+1]
ele=s-a[0]
l.append(ele)
s=0
for i in range(1,n-1):
    s+=a[i+1]
ele=s-a[1]-a[0]
l.append(ele)
s=0
for i in range(2,n-1):
    s+=a[i+1]
ele=abs(s-a[1]-a[0]-a[2])
l.append(abs(ele))
s=0
for i in range(3,n-1):
    s+=a[i+1]
ele=abs(s-a[1]-a[0]-a[2]-a[3])
l.append(ele)
s=0
for i in range(0,n):
    s+=a[i]
l.append(s)
print(l)
'''























n=int(input())
a=list(map(int,input().split()))
l=[]
tot=0
ls=0
rs=0
for i in a:
    tot+=i
for i in a:
    ls+=i
    rs=tot-ls
    cs=abs(rs-ls)
    l.append(cs)
print(l)
    

5
1 2 3 4 5
[13, 9, 3, 5, 15]

















