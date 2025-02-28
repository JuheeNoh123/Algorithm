import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n=int(input())
L = list(map(int, input().split()))

def gcd(a,b):
    #print(a,b)
    if b==0:
        return a
    return gcd(b,a%b)    

h = []    
for i in combinations(L,n-1):
    h.append(i)
#print(h)
ans=[1 for _ in range(n)]
d = 1#분자자
for i in range(n):
    for j in h[i]:
        ans[i] *= j
    d*=L[i]
m=sum(ans)#분모모

if d>m:
    cd=gcd(d,m)
else:
    cd=gcd(m,d)

print(d//cd,'/',m//cd,sep='')
