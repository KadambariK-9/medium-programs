#BEST GRADE
'''
print(' '.join(s!))..from list to string


cbagafg
INPUT
abcdefg
3........c
2...swaps
OUTPUT
a




s=input()
n1=int(input())
n2=int(input())
mn=999
l=list(s)
a=''
for i in range(1,len(s)+1):
    l[n1]
    if ord(i)<mn:
        mn=ord(i)
        a+=i
print(a)

'''



s=input()
p=int(input())
k=int(input())
s1=list(s)
s2=0
e=len(s1)
mini=999
if abs(p-k-1)>=0:
    s2=abs(p-k-1)
if p+k<len(s1):
    e=p+k
print(s2,e)
for i in range(s2,e):
    mini=min(ord(s1[i]),mini)
print(s1)
store=s1[p-1]
s1[p-1]=s1[s1.index(chr(mini))]
s1[s1.index(chr(mini))]=store
print(s1)
print(mini)
print(''.join(s1))









'''

s=input()
n1=int(input())
n2=int(input())
mn=999
a=''
l=list(s)
for i in range(0,len(s)+1):
    if n2!=0:
        a+=s[n1-1]
        n1+=1
        n2-=1
print(a)
for i in range(len(l)):
    if mn>ord(l[i]):
        mn=ord(l[i])
        a+=l[i]
    if l[i] not in a:
        a+=l[i]
print(a)






abcdefg
3
1
c
cabdefg


abcdefg
3
2
cd
cdabefg


'''







