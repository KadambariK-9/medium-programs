#MISSING ALPHABETS
'''
INPUT
WELCOME TO GEEKSFORGEEKS...........FROM A TO Z
OUTPUT
ABDHIJNPQUVXYZ.........THESE ARE MISSING FROM A-Z
'''
alpha='abcdefghijklmnopqrstuvwxyz'
inp=input()
c=''
for i in alpha:
    if i not in inp:
        c+=i
print(c)

'''
abd
cefghijklmnopqrstuvwxyz

welcome to
abdfghijknpqrsuvxyz

welcome to geeksforgeeks
abdhijnpquvxyz
'''
