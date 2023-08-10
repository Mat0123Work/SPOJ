# https://pl.spoj.com/problems/FLAMASTE/

def compress(line: str):
    result = ""
    currentLetter = ""
    currentCounter = 0
    for letter in line:
        if(letter == currentLetter):
            currentCounter +=1
        else:
            if(currentCounter > 2):
                result += currentLetter + str(currentCounter)
            else:
                result += currentCounter * currentLetter
            currentLetter = letter
            currentCounter = 1
    if(currentCounter > 2):
        result += currentLetter + str(currentCounter)
    else:
        result += currentCounter * currentLetter
    return result

C = int(input())

while(C > 0):
    line = input()
    print(compress(line))
    C-=1

