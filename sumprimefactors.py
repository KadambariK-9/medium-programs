#SUM OF PRIME FACTORS
'''
INPUT
6......SIZE OF ARRAY
11 21 32 45 1 23
6..PRIME FACTOR

OUTPUT
77
EXPLAINATION
6=2^1*3^1
SUM=1*ARR[2]+1*ARR[3]=1*32+1*45=77
'''











def pf(n):
    ans=[]
    i=2
    while i<=n:
        if n%i==0:
            ans.append(i)
            n=n//i
        else:
            i=i+1
    return ans
ans=pf(6)
s=0
a=[11,21,32,45,1,23]
for i in ans:
    s=s+a[i]
print(s)



77


'''
n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
x=2
for i in a:
    if n2%2==0:
        c=n2//x
    else:
         x+=1
print(x)
         


'''

















