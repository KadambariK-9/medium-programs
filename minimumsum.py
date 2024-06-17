#PROBLEM STATEMENT
#MINIMUM SUM AMONG BOTH SALT AND PEPPER
'''
INPUT
3
1 3 5.........SALT CONTAINER
2 8 6....PEPPER CONTAINER
OUTPUT
3



n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
mx=999
for i in range(n):
    sum=a1[i]+a2[i]
    if mx>sum:
        mx=sum
print(mx)
    


3
1 3 5
2 8 6
3

'''






n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
mn=999
for i in range(n):
    if a1[i]+a2[i]<mn:
        mn=a1[i]+a2[i]
print(mn)



3
1 3 5
2 8 6
3

