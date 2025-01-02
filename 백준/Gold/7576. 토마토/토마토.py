import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())
dx, dy = [-1,1,0,0],[0,0,1,-1]
L = []
queue = deque()
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and L[nx][ny]==0:
                L[nx][ny]=L[x][y]+1
                queue.append([nx,ny])
    #print(L)
    
for i in range(N):
    L.append(list(map(int, input().split())))
#print(L)

for i in range(N):
    for j in range(M):
        if L[i][j]==1:
            queue.append([i,j])
bfs()           
res=0
for i in L:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)