def areCollinear(x1, y1, x2, y2, x3, y3):
    return x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) == 0
    # (1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|

t = int(input())

while(t>0):
    x1, y1, x2, y2, x3, y3 = (float(x) for x in input().split())
    print("TAK") if areCollinear(x1,y1,x2,y2,x3,y3) else print("NIE")
    t-=1


