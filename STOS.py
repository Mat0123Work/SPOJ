# https://pl.spoj.com/problems/STOS/

stack = []

while True:
    try:
        inpt = input()
        if(inpt == "+"):
            continue
        elif(inpt == "-"):
            if(len(stack)>0):
                print(stack.pop())
            else:
                print(":(")
        else:
            if(len(stack) == 10):
                print(":(")
            else:
                stack.append(inpt)
                print(":)")
        pass
    except EOFError:
        break