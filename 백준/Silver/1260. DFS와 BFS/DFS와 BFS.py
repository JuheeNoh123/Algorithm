import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1,n+1):
    graph[i].sort()
    
visited_dfs = [0]*(n+1)
def dfs(start):
    visited_dfs[start] = True
    print(start,end=' ')
    for i in graph[start]:
        if not visited_dfs[i]:
            visited_dfs[i] = True
            dfs(i)
        
dfs(v)
print()
visited_bfs = [0]*(n+1)
def bfs(start,visited):
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
bfs(v, visited_bfs)

