# https://pl.spoj.com/problems/GLUTTON/

t = int(input())

while(t>0):
    n, m = (int(x) for x in input().split())

    totalCookies = 0
    while(n>0):
        gluttonTime = int(input())
        totalCookies += 86400//gluttonTime
        n-=1
    totalPacks = totalCookies//m
    totalPacks += 1 if totalCookies % m != 0 else 0
    print(totalPacks)
    t-=1