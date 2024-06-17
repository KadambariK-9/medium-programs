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
mx=-999
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==18:
            if a[i]>a[j]:
                x=a[i]*a[j]
                if x>mx:
                    mx=x
                    k=a[i]
                    h=a[j]
print(mx,k,h)

'''
8
11 12 2 8 10 11 7 8
80 10 8

8
11 12 2 8 10 11 9 8
80 10 8
'''
