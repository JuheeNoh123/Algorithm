import sys
from  itertools import product
input = sys.stdin.readline
s,e = map(int, input().split())
ns, ne = len(str(s)), len(str(e))
cnt=0
for i in range(ns, ne+1):
    L = list(product([4,7], repeat=i))
    for n in L:
        num = int(''.join(map(str,n)))
        
        if s<=num<=e:
            cnt += 1
print(cnt)