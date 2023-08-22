# https://pl.spoj.com/problems/PTCLTZ/

def calcN(s):
    n = 0
    result = s
    while(result != 1):
        if(result % 2 == 1):
            result = 3*result + 1
        else:
            result //= 2
        n+=1
    return n

t = int(input())

while(t>0):
    s = int(input())

    print(calcN(s))

    t-=1