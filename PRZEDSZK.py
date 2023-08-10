# https://pl.spoj.com/problems/PRZEDSZK/

def NWD(a, b):
    while (b > 0):
        q = a // b; 
        r = a - q * b
        a = b
        b = r
    return a

def NWW(a,b):
    return a*b//NWD(a,b)

n = int(input())
while(n>0):
    k,l = (int(x) for x in input().split())
    print(NWW(k,l))
    n-=1