import sys
from itertools import permutations
input = sys.stdin.readline
n,s = map(int, input().split())
L = list(map(int,input().split()))
l, r = 0,0
sum =0
m = 1e9
while True:
    if sum >= s:
        m = min(m, r-l)
        sum -= L[l]
        l +=1
    elif r==n:
        break
    else:
        sum += L[r]
        r+=1

if m==1e9:
    print(0)
else:
    print(m)