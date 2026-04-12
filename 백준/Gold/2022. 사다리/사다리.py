import sys
input = sys.stdin.readline

from math import sqrt

x,y,c = map(float, input().split())
start, end = 0, min(x,y)

def get(m):
    a = sqrt(x**2 - m**2)
    b = sqrt(y**2 - m**2)
    
    return a*b/(a+b)

res= 0

while end-start>1e-6:
    mid = (start+end)/2
    if get(mid) >= c:
        res = mid
        start = mid
    else:
        end = mid
print("{}".format(round(res,4)))