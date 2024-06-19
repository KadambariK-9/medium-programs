#REVERSE THE ORDER OF STRING
'''
INPUT
HELLO WORLD
OUTPUT
WORLD HELLO




s=input()
l=list(s)
i=0
j=len(l)-1
while i<=j:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i+=1
    j-=1
print(''.join(l))





s=input()
l=list(s)
lt=[]
n=len(l)
for i in range(len(s)):
    lt.append(l[n-1])
    n=n-1
print(lt)
print(''.join(lt))

['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
dlrow olleh








'''
s=input().split()
l=list(s)
lt=[]
n=len(s)
for i in range(len(s)):
    lt.append(l[n-1])
    n=n-1
print(lt)
print(' '.join(lt))



['efg', 'abcd']
efg abcd







s=input().split()
l=list(s)
a=' '
n=len(s)
for i in range(len(s)):
    a+=l[n-1]
    n=n-1
print(a)
















s=input().split()
s=s[::-1]
print(*s,sep='')
'''
