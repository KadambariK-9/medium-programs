#ROBO RACE
'''
2 3 1 4....
X=2 N=3 Y=1 M=4
N AND M ARE IN SECONDS
X IS STARING POINT OF ROBOT 1.....2,2+3=5,5+3=8,..
Y IS STARING POINT OF ROBOT 2.....1,1+4=5,5+4=9,.........
BOTH MEET AT 5.........OUTPUT
INPUT
2 3 1 4..shd give seperate
OUTPUT
5...SECONDS
'''

x,n,y,m=map(int,input().split())
time=max(x,y)
while True:
    if time>=x and (time-x)%n==0 and time>=y and (time-y)%m==0:
        print(time)
        break
    time+=1



2 3 1 4
5

3 3 1 4
9
