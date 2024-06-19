#SMALLEST NUMBER
'''
INPUT
50 66 23
OUTPUT
SMALLEST IS 23
'''
a=list(map(int,input().split()))
mn=999
for i in a:
    if mn>i:
        mn=i
print(mn)





50 66 23
23
