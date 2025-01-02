import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
L=[]
for i in range(N):
    A = list(map(int, input().strip()))
    L.append(A)
#print(L)
dx, dy = [-1,1,0,0] ,[0,0,-1,1]
visited = [[False] * N for _ in range(N)]
def bfs(a,b):
    cnt=1
    queue = deque([(a,b)])
    visited[a][b] = True
    #print(queue)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<N and 0<=ny<N and L[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny))
                cnt +=1
        
    #print(L)
    #print(cnt)
    return cnt
    

nL = []
xnt = 0
for i in range(N):
    for j in range(N):
        if L[i][j]==1 and not visited[i][j]:
            xnt+=1
            nL.append(bfs(i,j))
            bfs(i,j)
            
print(xnt)
nL.sort()
for i in nL:
    print(i)
        
            
            
