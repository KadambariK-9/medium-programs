#MAGIC STRING
'''
INPUT
AAABBBCCDDDD.............MAXIMUM REPETITION IS D SO IF D IS CONSIDERED TO REPLACE THEN IT TAKES
MINIMUM NUMBER OF STEPS TO REPLACE D........IT TAKES 8 STEPS....C...........10...........
A AND B.....9 STEPS SO AMONG ALL THESE MINIMUM IS 8
OUTPUT
8
'''
a=input()
d={}
c=0
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    if d[i]>c:
        c=d[i]
print(len(a)-c)





aaabbbccdddd
8

aaabb
2
