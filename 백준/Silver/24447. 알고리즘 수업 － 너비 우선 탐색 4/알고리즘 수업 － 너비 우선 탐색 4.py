import sys
from collections import deque
input = sys.stdin.readline


n,m,r = map(int, input().split())
g = [[] for i in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in range(1,n+1):
    g[i].sort()

cnt = [-1]*(n+1)
d = [0]*(n+1)
def bfs(r):
    
    visited[r]=True
    queue = deque([r])
    cnt[r] = 0
    d[r]=1
    #print(queue)
    turn = 1
    while queue:
        nq = queue.popleft()
        
        for i in g[nq]:
            
            if visited[i] == False:
                #print(i)
                visited[i] = True
                cnt[i] = cnt[nq]+1
                d[i] = turn+1
                turn += 1
                queue.append(i)
        
bfs(r)
sum=0
for i in range(1,n+1):
    
    sum += cnt[i]*d[i]
print(sum)