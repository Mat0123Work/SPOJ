def countSols(a,b,c):
    delta = b*b - 4*a*c
    if(delta > 0): return 2
    elif(delta == 0): return 1
    else: return 0


while True:
    try:
        inpt = input()
        a,b,c = (float(x) for x in inpt.split())
        print(countSols(a,b,c))
    except EOFError:
        break