#VOWEL REPETITION PROBLEM
'''
INPUT
HELLOWORLD
OUTPUT
O
'''
d={}
a=input()
v='aeiou'
ans=0
mx=-999
for i in a:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(d)
print(ans)




helloworld
{'e': 1, 'o': 2}
o

heeelooooo
{'e': 3, 'o': 5}
o

aaaaaaee
{'a': 6, 'e': 2}
a






            
