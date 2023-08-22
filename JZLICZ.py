# https://pl.spoj.com/problems/JZLICZ/

slownikLiter = {}
klucze = []

n = int(input())

while(n>0):
    linijka = input()
    for character in linijka:
        if(character.isalpha()):
            if(character in slownikLiter):
                slownikLiter[character]+=1
            else:
                slownikLiter[character] = 1
                klucze.append(character)
    n-=1

klucze.sort(key=str.swapcase)
for key in klucze:
    print(key+ " " + str(slownikLiter[key]))
