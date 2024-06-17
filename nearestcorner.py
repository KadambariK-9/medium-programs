#NEAREST CORNER
'''
INPUT
3C
1A 2B - 3C 4D
OUTPUT
0

1A - 2B 3C 4D 5E - 6F

'''
chair=input()
a=list(input().split())
z=999#we want minimum
c_ind=a.index(chair)
for i in range(0,c_ind):
    if a[i]=='-':
        if abs(c_ind-i)-1<z:
            z=abs(c_ind-i)-1
for i in range(c_ind+1,len(a)):
    if a[i]=='-':
        if abs(i-c_ind)-1<z:
            z=abs(i-c_ind)-1
print(z)





4d
1a 2b - 3c 4d 5e - 6f
1

3c
1a 2b - 3c 4d
0

