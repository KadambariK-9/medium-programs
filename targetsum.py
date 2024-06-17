#TARGET SUM
'''
INPUT
2 7 11 15
9.............TARGET SUM
OUTPUT
[0,1].......2+7=9.......SO 0 AND 1 AS OUTPUT
'''
a=list(map(int,input().split()))
t=int(input())
a.sort()
i=0
j=len(a)-1
ans=0
while i<j:
    curr_sum=a[i]+a[j]
    if curr_sum==t:
        print(i,j)
        i+=1
        j-=1
    elif curr_sum<t:
        i+=1
    else:
        j-=1



15 11 2 7
9
0 1





