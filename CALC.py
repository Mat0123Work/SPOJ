def evaluate(op,a,b):
    if(op == "+"): return a+b
    if(op == "-"): return a-b
    if(op == "*"): return a*b
    if(op == "/"): return a//b
    if(op == "%"): return a%b
    return 0

t = 100
while(t>0):
    operand,a,b = input().split()
    a,b = int(a),int(b)
    print(evaluate(operand,a,b))
    t-=1