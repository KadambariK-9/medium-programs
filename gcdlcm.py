#SIGNATURE OF LCM
'''
INPUT
12 18
OUTPUT
6............GCD
36..............LCM



def gcd(a,b):
    while b!=0:
        temp=a
        a=b
        b=b%temp
    return a
def lcm(a,b):
    x=gcd(a,b)
    ans=(a*b)//x
    return ans
a,b=map(int,input().split())
res=gcd(a,b)
r=lcm(a,b)
print(res)
print(r)



12 18
6
36
'''
