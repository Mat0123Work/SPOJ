# https://pl.spoj.com/problems/ETI06F1/

PI = 3.141592654
r,d = (float(x) for x in input().split())
R_SQ = r*r - d*d/4.0

print(round(PI * R_SQ, 2))



