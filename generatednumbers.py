#GENERATED NUMBERS
'''
10=0*3+0*5
10=0*3+1*5
10=1*3+0*5
10=1*3+1*5
10=2*3+0*5
10=3*3+0*5
INPUT
10 3 5...N A B
OUTPUT
6
'''

n,a,b=map(int,input().split())
c=0
for i in range(0,n//a+1):
    for j in range(0,n//b+1):
        if (i*a+j*b)<n:
            c+=1
print(c)



10 3 5
0 '
5 '
3 '
8 '
6 '
9 ''''possibilities

6..ans

10 3 5
6















