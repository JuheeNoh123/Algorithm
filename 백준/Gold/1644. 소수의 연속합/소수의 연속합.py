import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
L = [False, False]+[True]*(n-1)
p = []
for i in range(2,n+1):
    if L[i]:
        p.append(i)
        for j in range(2*i,n+1,i):
            L[j]=False
            
# print(L)
# print(p)
r,l =0,0
ans=0
while r<=len(p):
    s = sum(p[l:r])
    if s==n:
        ans+=1
        r+=1
    elif s<n:
        r+=1
    else:
        l+=1
    #print(r,l)
print(ans)