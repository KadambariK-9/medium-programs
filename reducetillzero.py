#REDUCE TILL ZERO
'''
1. IF X<Y INTERCHANGE
2. IF Y=0 THEN RETURN X
3. OTHERWISE LET T=X-Y
4. SET X=Y AND THEN SET Y=T
5. REPEAT FROM 1............UNTIL Y=0
INPUT
48
18
OUTPUT
6
'''
x=int(input())
y=int(input())
while y>0:
    if x<y:
        temp=x
        x=y
        y=temp
        #x,y=y,x
    t=x-y
    x=y
    y=t
print(x)
    
48
18
6
   
