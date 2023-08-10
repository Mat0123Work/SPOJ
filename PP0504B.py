# https://pl.spoj.com/problems/PP0504B/


def concat(a,b):
    lenA = len(a)
    lenB = len(b)
    minLen = min(lenA,lenB)

    result = ""
    for i in range(minLen):
        if(i == lenA): return result
        result += a[i]
        if(i == lenB): return result
        result += b[i]
    return result

t = int(input())
while(t>0):
    left,right = input().split()
    print(concat(left,right))
    t-=1