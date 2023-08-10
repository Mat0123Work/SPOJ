t = int(input())

while(t>0):
    v1,v2 = (int(x) for x in input().split())
    print(2*v1*v2//(v1+v2))
    t-=1