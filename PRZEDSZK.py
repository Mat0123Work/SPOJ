
# dzielniki = [
#     {2, 5, 10},
#     {11},
#     {2, 3, 4, 6, 12},
#     {13},
#     {2, 7, 14},
#     {3, 5, 15},
#     {2, 4, 8, 16},
#     {17},
#     {2, 3, 6, 9, 18},
#     {19},
#     {2, 4, 5, 10, 20},
#     {3, 7, 21},
#     {2, 11, 22},
#     {23},
#     {2, 3, 4, 6, 8, 12, 24},
#     {5, 25},
#     {2, 13, 26},
#     {3, 9, 27},
#     {2, 4, 7, 14, 28},
#     {29},
#     {2, 3, 5, 6, 10, 15, 30},
# ]

# def dividable():
#     for i in range(10, 31):
#         print(f"[", end="")
#         for j in range(2, i+1):
#             if(i%j == 0):
#                 print(str(j)+",", end=" ")
#         print("],")

#dividable()
# N = int(input())
# while(N > 0):
#     a,b = (int(x) for x in input().split())
#     zbiorA = dzielniki[a-10]
#     zbiorB = dzielniki[b-10]
#     sumaZbiorow = zbiorA.union(zbiorB)
#     wynik = 1
#     for elem in sumaZbiorow:
#         wynik *= elem
#     print(wynik)
#     N-=1

def NWD(a, b):
    while (b > 0):
        q = a // b; 
        r = a - q * b
        a = b
        b = r
    return a

def NWW(a,b):
    return a*b//NWD(a,b)

n = int(input())
while(n>0):
    k,l = (int(x) for x in input().split())
    print(NWW(k,l))
    n-=1