import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
L = [list(input().strip()) for _ in range(n)]
dx,dy = [0,0,1,-1],[1,-1,0,0]
def bfs(i,j):
    #print(i,j)
    cnt=0
    visited = [[0 for _ in range(m)]for _ in range(n)]
    #print(visited)
    queue = deque([(i,j)])
    visited[i][j]=1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if L[nx][ny] !='X':
                    if L[nx][ny]=='P':
                        cnt += 1
                    visited[nx][ny]=1
                    queue.append((nx,ny))
                    #print(visited)
    return cnt
            
            
for i in range(n):
    for j in range(m):
        if L[i][j]=='I':
            ans = bfs(i,j)

if ans==0:
    print('TT')
else:
    print(ans)