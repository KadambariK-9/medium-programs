#FINDING COMMAS
'''INPUT
5000
OUTPUT
4001......THE COMMAS ARE USED FROM 4 DIGIT SO
FOR 999 NO COMMAS FROM 1000 COMMAS ARE THERE
SO OUTPUT =5000-4001
from right only after 3 digit comma
1,000...1,000,000...1,000,000,000
k=1 ans=1
c=1000
n=1010000
c<n
m=1000000
nums=min(1009001,999000)
ans=999000
c=m
k=2



k=2
ans=999000
c=1000000
n=1010000
c<n
m=1,000,000,000
nums=min(10001,90000000)
ans=200002
c=m
k=3
'''
n=int(input())
c=1000
k=1
ans=0#1
s=0
while c<n:
    m=c*1000
    num=min(n-c+1,m-c)
    ans=num*k#ans+=num*k
    s+=ans
    c=m
    k+=1
print(s)


'''
5000
4001

1010000
1019002
'''
