#MINIMUM NUMBER OF KEY PRESSES
'''
INPUT
100.....................(0,1,2,3,4,5,6,7,8,9,00)
OUTPUT
2..........ONCE 1 AND AGAIN.......00 ONCE SO ......2 TIMES PRESSED

7690090...........6 TIMES KEY PRESSED
'''
s=input()
i=0
c=0
while i<len(s)-1:
    if s[i]=='0' and s[i+1]=='0':
        c+=1
        i+=2
    else:
        c+=1
        i+=1
if i<len(s):
    c+=1
print(c)
                       
1000
3

10
2

100
2
