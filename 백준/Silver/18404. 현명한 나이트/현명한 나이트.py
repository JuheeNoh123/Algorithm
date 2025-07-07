import sys 
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
k_x, k_y = map(int, input().split())
L = list(list(map(int, input().split())) for _ in range(m))
A = [0 for _ in range(m)]
#print(L)
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
def bfs(sx,sy):
    dx=[-2,-2,-1,-1,1,1,2,2]
    dy=[-1,1,-2,2,-2,2,-1,1]
    
    queue = deque([(sx,sy)])
    
    #visited[sx][sy]=1
    while queue:
        #print(queue)
        x,y = queue.popleft()
        
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<=n and 0<nx and ny<=n and 0<ny and visited[nx][ny]==0:
                queue.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1
                # for j in range(m):
                #     if L[j][0]==nx and L[j][1]==ny:
                #         A[j]=visited[nx][ny]
                        
                #print(A)
bfs(k_x,k_y)

for i in L:
    print(visited[i[0]][i[1]], end = ' ')