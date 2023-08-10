# https://pl.spoj.com/problems/PP0502B

t = int(input())
while(t>0):
    lineNumbers = input().split()[1:]
    print(" ".join(lineNumbers[::-1]))
    t-=1