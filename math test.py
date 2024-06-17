def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
k=n+1
while True:
    if isprime(k):
        print(k)
        break
    k=k+1

7
11
