#SPECIAL FIBONACCI
'''
2=2
3=2*2+1=5
4=25+4=29
5=29*29+25%47=20
6=20*20+29%47=19
'''
'''
#recursive
def f(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (f(n-1)*f(n-1)+(n-2)*(n-2))%47
num=int(input())
res=f(num)
print(res)

6
34
'''










#iterative
x=[1,1]
inp=int(input())
for i in range(2,inp+1):
    ans=(x[i-1]*x[i-1]+(i-2)*(i-2))%47
    x.append(ans)
print(x[inp])



6
34

















