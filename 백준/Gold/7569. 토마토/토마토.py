import sys
from collections import deque
input = sys.stdin.readline

N,M,H = map(int,input().split())
field = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]
queue = deque()
dx,dy, dz = [0,0,1,-1,0,0],[1,-1,0,0,0,0], [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx, ny,nz= x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and not field[nz][nx][ny]:
                field[nz][nx][ny]=field[z][x][y]+1
                queue.append([nz, nx,ny])
            


for i in range(H):
    for j in range(M):
        for k in range(N):
            if field[i][j][k]==1:
                queue.append([i,j,k])
     
bfs()

res=0
for i in field:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
            res = max(res,k)
    
print(res-1)