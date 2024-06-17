#FELLIS FUNCTION
'''
F(0)=1
F(1)=1
F(N)=F(N-1)+7*(N-2)+(N/4)MODULO 10^9+7




#recursive

def f(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (f(n-1))+(7*f(n-2))+(n//4)%(10**9+7)
num=int(input())
res=f(num)
print(res)
    
8
6713





#iterative

n=int(input())
l=[1,1]
for i in range(2,n+1):
    ans=(l[i-1]+7*l[i-2]+i//4)%(10**9+7)
    l.append(ans)
print(l[n])
    
8
6713

'''










