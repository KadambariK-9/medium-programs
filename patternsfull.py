#PATTERN
'''
    *
  * *
* * *
* * *
  * *
    *
'''
for i in range(1,4):
    for s in range(1,3-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print()



for i in range(3,0,-1):
    for s in range(0,3-i):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print()


  *
 **
***
***
 **
  *

