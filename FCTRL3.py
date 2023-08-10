# https://pl.spoj.com/problems/FCTRL3/

digits= ["0 1", "0 1", "0 2", 
          "0 6", "2 4", "2 0", 
          "2 0", "4 0", "2 0", 
          "8 0"]

# 0! = 0
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362 880
# 10! = 

def lastTwoDigitsOfFactorial(n):
    if(n < 10): return digits[n]
    return "0 0"

n = int(input())

while(n>0):
    k = int(input())
    print(lastTwoDigitsOfFactorial(k))
    n-=1