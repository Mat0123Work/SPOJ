def calcDistanceSquared(elem):
    return elem[1]**2 + elem[2]**2

def insertToList(elem, li):
    distance = calcDistanceSquared(elem)
    newElem = elem + (distance,)
    for i in range(len(li)):
        if(li[i][3] > distance):
            li.insert(i, newElem)
            return
    li.append(newElem)

try:
    t = int(input())

    while(t>0):
        n = int(input())
        result = []
        while(n>0):
            name, x, y = input().split()
            x = int(x)
            y = int(y)
            elem = (name, x, y)
            insertToList(elem, result)  
            n-=1
        for i in range(len(result)):
            print(f"{result[i][0]} {result[i][1]} {result[i][2]}")
        t-=1
except EOFError:
    pass


