#MINIMUM ARRAY SUM
'''
INPUT
[12,16,2,23,1]
OUTPUT
GREATEST AND 2ND GREATEST
LIKE 23 AND 16
'''



'''
l=[12,16,2,23,18]
for i in range(4):
    mx=l[i]
    if mx<l[i+1]:
        mx=l[i+1]
print(mx)
for i in range(4):
    mx2=l[i]
    if mx2<l[i+1]:
        mx2=l[i+1]
if mx2!=mx
    print(mx2)
if mx2!=mx:
    print(mx2)







a=list(map(int,input().split()))
mx=-999
mx2=-999

for i in a:
    if i>mx:
        mx=i
print(mx)
for i in a:
    if i>mx2 and i!=mx:
        mx2=i
print(mx2)




12 16 2 23 18
23
18



12 16 2 23 1
23
16

'''

a=list(map(int,input().split()))
mx=-999
mx2=-999

for i in a:
    if i>mx:
        mx=i
print(mx)
for i in a:
    if i>mx2 and i!=mx:
        mx2=i
print(mx2)
avg=(mx+mx2)/2
ans=0
for i in a:
    if i>avg:
        ans+=i
print(ans)


12 16 2 23 1
23
16
23










