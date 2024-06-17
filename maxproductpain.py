#MAXIMIZE PAIR PRODUCT
'''
INPUT
8....SIZE
11 12 2 8 10 11 9 8
OUTPUT
[10,8].......SUM SHOULD BE 18 PRODUCT SHD BE MAXIMUM
'''
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]+a[i+1]==18:
        x=a[i]*a[i+1]
print(x)
