import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().split())
L = [[] for _ in range(n+1)]
d =[-1]*(n+1)
for i in range(1,m+1):
    s, e = map(int, input().split())
    L[s].append(e)
    L[e].append(s)
v = [0]*(n+1)
def bfs(s):
    queue= deque([s])
    v[s] = 1
    d[s]=0
    while queue:
        a = queue.popleft()
        for i in L[a]:
            if not v[i]:
                d[i] = d[a]+1
                v[i]=1
                queue.append(i)
                
    #print(d)
bfs(r)

for i in range(1,n+1):
    print(d[i])