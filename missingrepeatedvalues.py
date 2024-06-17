#FIND MISSING AND REPEATED VALUES
'''
INPUT
[[1,3],[2,2]]
OUTPUT
[2,4]..........2 IS REPEATED AND 4 IS MISSING NUMBER


#arr=np.array(a).reshape(2,3)
a=[]
for i in range(0,3):
    sub=[]
    print('enter values for row',i)
    for j in range(0,3):
        print('enter values for column',j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)




        
enter values for row 0
enter values for column 0
1
[1]
enter values for column 1
2
[1, 2]
enter values for column 2
3
[1, 2, 3]
[[1, 2, 3]]
enter values for row 1
enter values for column 0
4
[4]
enter values for column 1
5
[4, 5]
enter values for column 2
6
[4, 5, 6]
[[1, 2, 3], [4, 5, 6]]
enter values for row 2
enter values for column 0
7
[7]
enter values for column 1
8
[7, 8]
enter values for column 2
9
[7, 8, 9]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]














r=int(input())
c=int(input())
a=[]
#input
for i in range(0,r):
    sub=[]
    print('enter values for row',i)
    for j in range(0,c):
        print('enter values for column',j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
#repeated
d={}
ans=[]
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d: 
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)

#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)







#output

enter values for row 0
enter values for column 0
1
[1]
enter values for column 1
2
[1, 2]
enter values for column 2
3
[1, 2, 3]
[[1, 2, 3]]
enter values for row 1
enter values for column 0
4
[4]
enter values for column 1
5
[4, 5]
enter values for column 2
6
[4, 5, 6]
[[1, 2, 3], [4, 5, 6]]
enter values for row 2
enter values for column 0
6
[6]
enter values for column 1
8
[6, 8]
enter values for column 2
9
[6, 8, 9]
[[1, 2, 3], [4, 5, 6], [6, 8, 9]]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 8: 1, 9: 1}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 8: 1, 9: 1}
[6, 7]



'''
















r=int(input())
c=int(input())
a=[]
#input
for i in range(0,r):
    sub=[]
    print('enter values for row',i)
    for j in range(0,c):
        print('enter values for column',j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
#repeated
d={}
ans=[]
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d: 
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1//can be removed but same output
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)

#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)































