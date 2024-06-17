#POSSIBLE UNIQUE TRIPLETS PRODUCTS
'''
INPUT
7
5 3 20 10 1 4 2
60...................(5*4*3),(20*3*1),(10*3*2)
OUTPUT
3............COUNT OF UNIQUE TRIPLETS
'''
t=60
pr0=1
c=0
a=[5,3,20,10,1,4,2]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            print('indexes',i,j,k)
            print('values',a[i],a[j],a[k])
            pro=a[i]*a[j]*a[k]
            if pro==t:
                print(pro)
                print('triplet',a[i],a[j],a[k])
                c=c+1
        print()
print(c)









indexes 0 1 2
values 5 3 20
indexes 0 1 3
values 5 3 10
indexes 0 1 4
values 5 3 1
indexes 0 1 5
values 5 3 4
60
triplet 5 3 4
indexes 0 1 6
values 5 3 2

indexes 0 2 3
values 5 20 10
indexes 0 2 4
values 5 20 1
indexes 0 2 5
values 5 20 4
indexes 0 2 6
values 5 20 2

indexes 0 3 4
values 5 10 1
indexes 0 3 5
values 5 10 4
indexes 0 3 6
values 5 10 2

indexes 0 4 5
values 5 1 4
indexes 0 4 6
values 5 1 2

indexes 0 5 6
values 5 4 2


indexes 1 2 3
values 3 20 10
indexes 1 2 4
values 3 20 1
60
triplet 3 20 1
indexes 1 2 5
values 3 20 4
indexes 1 2 6
values 3 20 2

indexes 1 3 4
values 3 10 1
indexes 1 3 5
values 3 10 4
indexes 1 3 6
values 3 10 2
60
triplet 3 10 2

indexes 1 4 5
values 3 1 4
indexes 1 4 6
values 3 1 2

indexes 1 5 6
values 3 4 2


indexes 2 3 4
values 20 10 1
indexes 2 3 5
values 20 10 4
indexes 2 3 6
values 20 10 2

indexes 2 4 5
values 20 1 4
indexes 2 4 6
values 20 1 2

indexes 2 5 6
values 20 4 2


indexes 3 4 5
values 10 1 4
indexes 3 4 6
values 10 1 2

indexes 3 5 6
values 10 4 2


indexes 4 5 6
values 1 4 2



3
