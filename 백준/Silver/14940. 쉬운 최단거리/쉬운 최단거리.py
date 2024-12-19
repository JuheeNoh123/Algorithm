import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
dx, dy = [0,0,-1,1],[-1,1,0,0]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b]=0
    
    while queue:
        x,y = queue.popleft()
        
        
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==-1:
                if graph[nx][ny]==0:
                    visited[nx][ny]=0
                elif graph[nx][ny]==1:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1

for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()