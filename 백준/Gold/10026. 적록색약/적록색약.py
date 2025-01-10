import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    L = list(input().strip())
    graph.append(L)
    
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(sx, sy, color):
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    queue = deque([(sx,sy)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                
                if graph[nx][ny]==color:
                    visited[nx][ny]=1
                    queue.append((nx,ny))

    return visited


                        
                        

    return visited
cnt =0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j])
            cnt += 1
print(cnt, end=' ')

cnt=0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'
            
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,graph[i][j])
            cnt += 1
print(cnt)