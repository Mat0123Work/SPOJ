t = int(input())
suma = 0

while(t>0):
    n = int(input())
    liczby = [int(x) for x in input().split()]
    print(sum(liczby))
    t-=1