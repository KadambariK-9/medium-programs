#FIND THE SUM OF ENCRYPTED INTEGERS
'''
INPUT
1 2 3
OUTPUT
6


INPUT
10 21 31.......IN 10 1 IS GREATER SO 0 IS REOLACED BT 1  SO 11+22+33=66
OUTPUT
66



WITHOUT STRING
'''
takeyouforward.org
striver a to z dsa sheet

               sde sheet


a=[321,645,984]
def pro(n):
    mx=-999
    c=0
    ans=0
    while n>0:
        dig=n%10
        if dig>mx:
            mx=dig
        c=c+1
        n=n//10
    while c>0:
        ans=ans*10+mx
        c=c-1
    return ans
n=list(map(int,input().split()))
f_ans=0
for i in n:
    ans=pro(i)
    f_ans+=ans
print(f_ans)






321 642 984
1998











































mx=0
n=int(input())
n=n%10
print(n)
x=mx*10+mx
print(x)
