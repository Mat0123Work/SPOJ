def isPrime(n: int):
    if(n==1): return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

while(n>0):
    k = int(input())

    if(isPrime(k)):
        print("TAK")
    else:
        print("NIE")
    n-=1