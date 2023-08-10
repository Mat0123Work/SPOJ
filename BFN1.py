def czyPalindrom(liczbaStr: str):
    for i in range(len(liczbaStr)//2 + 1):
        if(liczbaStr[i] != liczbaStr[-i-1]): 
            return False
    return True

n = int(input())

while(n>0):
    liczbaStr = input()
    k = 0
    while(not czyPalindrom(liczbaStr)):
        revLiczba = liczbaStr[::-1]
        liczbaStr = str(int(liczbaStr) + int(revLiczba))
        k+=1
    print(liczbaStr, k)
    n-=1