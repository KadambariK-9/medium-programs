#TOSS AND SCORE
'''
IF H THEN +2
IF T THEN -1

IF IT IS CONTINOUSLY 3 HHH OR 3 TTT THEN END AND COUNT TILL THERE
INPUT
HHHTHT
OUTPUT
6

hthhth
'''

tc=0
hc=0
mx=0
a=input()
for i in a:
    if i.upper()=='H':
        tc=0
        hc+=1
        mx=mx+2
        if hc==3:
            break
    else:
        hc=0
        tc+=1
        mx=mx-1
        if tc==3:
            break
print(mx)






hhhthh
6

hhthh
7


