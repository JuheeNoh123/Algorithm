import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = 0
s =int(input())
L=input().strip()
idx=0
cnt=0
while idx<s-1:
    
    if L[idx:idx+3]=='IOI':
        idx+=2
        cnt+=1
        
        if cnt==n:
            ans+=1
            cnt-=1
    else:
        idx+=1
        cnt=0


print(ans)