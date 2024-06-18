#SOLVE THE EQUATION
'''
INPUT
6
OUTPUT
1
'''
n=int(input())
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            fun=i**2+j**2+k**2+i*j+j*k+k*i
            if n==fun:
                print(i,j,k)
                f=1        
if f==0:
    print('not posibble')
else:
    
    print('possible',f)


'''
6
1 1 1
possible  1
'''
