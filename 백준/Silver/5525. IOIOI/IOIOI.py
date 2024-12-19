import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = 'IOI'+('OI'*(n-1))
s =int(input())
L=input().strip()
idx=0
cnt=0
while idx<s:
    for i in range(idx,s):
        if L[i]=='I':
            idx=i
            break
    if L[idx:idx+2*n+1]==ans:
        cnt+=1
    idx+=1



print(cnt)