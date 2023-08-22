suma = 0
while(True):
    try:
        inpt = input()
        suma += int(inpt)
        print(suma)
    except EOFError:
        break
