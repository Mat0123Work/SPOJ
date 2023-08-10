pows = [
    [0], # 0
    [1], # 1
    [2,4,8,6], # 2
    [3, 9, 7, 1], # 3
    [4, 6], # 4
    [5], # 5
    [6], # 6
    [7,9,3,1], # 7
    [8,4,2,6], # 8
    [9,1] # 9
]

def powLastDigit(a,b):
    lastDigit = a%10
    choosenList = pows[lastDigit]
    strippedB = (b-1)%len(choosenList)
    return choosenList[strippedB]

t = int(input())

while(t>0):
    a,b = (int(x) for x in input().split())
    print(powLastDigit(a,b))
    t-=1
