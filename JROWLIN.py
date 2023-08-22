a, b, c = (float(x) for x in input().split())

if(a != 0):
    print("{:.2f}".format(round((c-b)/a,2)))
else:
    if(b == c):
        print("NWR")
    else:
        print("BR")