import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

L = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if L[i][j]==9:
            sx,sy = i,j
            L[sx][sy]=0
            break
scale = 2
def bfs():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    di=[0,0,1,-1]
    dj=[1,-1,0,0]
    q = deque([(sx,sy)])
    visited[sx][sy]=0
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<n and 0<=nj<n:
                if scale>=L[ni][nj] and visited[ni][nj]==-1:
                    visited[ni][nj] = visited[i][j] +1
                    q.append([ni,nj])
                
    return visited
INF = 1e9
def solve(visited):
    x,y = 0,0
    min_distance = INF
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=-1 and 1<=L[i][j]<scale:
                if visited[i][j]<min_distance:
                    min_distance = visited[i][j]
                    x,y = i,j
    if min_distance==INF:
        return False
    else:
        return x,y,min_distance

food = 0
ans=0
while True:
    res = solve(bfs())
    if not res:
        print(ans)
        break
    else:
        sx, sy = res[0], res[1]
        ans += res[2]
        L[sx][sy]=0
        food+=1
        
    if food>= scale:
        scale +=1
        food=0
