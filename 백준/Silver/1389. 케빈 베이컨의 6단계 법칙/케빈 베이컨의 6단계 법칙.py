import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
L=[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)
    
#print(L)


def bfs(start,n,visited):
    H = [0 for _ in range(n+1)]
    queue = deque([start])
    visited[start]=True
    
    while queue:
        x = queue.popleft()
        #print(x)
        for i in L[x]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                H[i] = H[x]+1
                #print(H)
    return sum(H)

M = 10000000000
idx=0
for i in range(1,n+1):
    visited=[False] * (n+1)
    #print(i,'===')
    ans = bfs(i,n,visited)
    if ans<M:
        M=ans
        idx=i
print(idx)