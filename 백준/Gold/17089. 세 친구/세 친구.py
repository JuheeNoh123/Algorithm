import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
frd=[[False for _ in range(n)] for _ in range(n)]
cnt = [0 for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    frd[a-1][b-1] = True
    frd[b-1][a-1] = True
    cnt[a-1] += 1
    cnt[b-1] += 1
res=12001
for i in range(n):
    for j in range(i+1,n):
        if not frd[i][j]:
            continue
        for k in range(j+1,n):
            if not frd[i][k] or not frd[j][k]:
                continue
            res = min(res,cnt[i]+cnt[j]+cnt[k]-6)
        
if res==12001:
    print(-1)
else:
    print(res)