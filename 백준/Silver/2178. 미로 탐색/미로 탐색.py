import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
L=[]
for i in range(M):
    A = list(map(int, input().strip()))
    L.append(A)
#print(L)
dx, dy = [-1,1,0,0] ,[0,0,-1,1]
queue = deque([(0,0)])
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y
            if 0<=nx<M and 0<=ny<N and L[nx][ny]==1:
                L[nx][ny]=L[x][y]+1
                queue.append([nx,ny])

bfs()
print(L[-1][-1])