# https://pl.spoj.com/problems/SKARBFI/

def moveInDir(currX, currY, dir, count):
    if(dir == 0):
        return [currX, currY+count]
    elif(dir == 1):
        return [currX, currY-count]
    elif(dir == 2):
        return [currX-count, currY]
    elif(dir == 3):
        return [currX+count, currY]

t = int(input())

while(t>0):
    n = int(input())
    currX, currY = 0, 0
    while(n>0):
        dir, count = (int(x) for x in input().split())
        currX, currY = moveInDir(currX, currY, dir, count)
        n-=1
    if(currX == 0 and currY == 0): print("studnia")
    else:
        if(currY != 0):
            print(f"{0 if currY > 0 else 1} {currY if currY > 0 else -currY}")
        if(currX != 0):
            print(f"{3 if currX > 0 else 2} {currX if currX > 0 else -currX}")
    t-=1