#PEAK ELEMENT
'''
INPUT
5
1 3 20 4 1
OUTPUT
2

1 3 2 20 4 6 5 1

'''
a=list(map(int,input().split()))
mx=0
for i in range(1,len(a)):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        p=a[i]
        if p>mx:
            mx=p
print(mx)



1 3 20 4 1
20

1  2 20 4 6 5 1
20
