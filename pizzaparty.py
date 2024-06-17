#PIZZA PARTY
'''
INPUT
100 17....100 CHOCOLATES....17 PEOPLE I WANT 3 EXTRA
BECAUSE PIZZAS SHOULD BE SHARED EQUALLY SO 17+3=20
2+0=2..OUTPUT
OUTPUT
2
'''



'''
n1,n2=map(int,input().split())
while n1>n2:
    if n1%n2==0:
        c=n1//n2
        print(c)
        break
    else:
        n2+=1
print(n2)
ans=n2//10
print(ans)
''' 


n1,n2=map(int,input().split())
ans=0
while True:
    if n1%n2==0:
        ans=n2
        break
    else:
        n2+=1
s=0
while ans>0:
    dig=ans%10
    s=s+dig
    ans=ans//10
print(s)






50 22
7

100 17
2






































