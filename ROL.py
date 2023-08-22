def shiftLeft(tab):
    if(len(tab) == 0): return tab
    zeroElem = tab[0]
    for i in range(len(tab)-1):
        tab[i] = tab[i+1]
    tab[len(tab)-1] = zeroElem
    return tab

t = int(input())

while(t>0):
    tab = shiftLeft([int(x) for x in input().split()[1::]])

    for elem in tab:
        print(str(elem)+" ", end="")
    print()
    t-=1