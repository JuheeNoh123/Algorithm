import sys
from collections import deque
input=sys.stdin.readline

t = int(input())
pos_x = [-1,1,0,0]
pos_y = [0,0,-1,1]
  
def BFS(x,y):
    queue = deque([(x,y)])
    field[x][y] = 0
    
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx+pos_x[i]
            ny = vy+pos_y[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if field[nx][ny]==1:
                field[nx][ny]=0
                queue.append((nx,ny))
    
for _ in range(t):
    cnt =0
    m,n,k = map(int, input().split())
    field = [[0]*(n) for _ in range(m)]
    for i in range(k):
        x,y = map(int, input().split())
        field[x][y] = 1
    
    for a in range(m):
        for b in range(n):
            if field[a][b]==1:
                BFS(a,b)
                cnt += 1       
                
    print(cnt)

    


