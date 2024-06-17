#SUBARRAY WITH MAX SUM
'''
INPUT
8...........SIZE
-1 2 3 10 -4 7 2 -5
OUTPUT
20.........[2,3,10,-4,7,2]..SUBARRAY WITH MAXIMUM 20  2 4 6 -13 9 8 2
2 4 6 -13 9 8 2
'''

a=list(map(int,input().split()))
mx_sum=0
c_sum=0
for i in a:
    c_sum+=i
    if c_sum<0:
        c_sum=0
    if c_sum>mx_sum:
        mx_sum=c_sum            #kadanes algorithm
print(mx_sum)




2 4 6 -13 9 8 2
19

-1 2 3 10 -4 7 2 -5
20
