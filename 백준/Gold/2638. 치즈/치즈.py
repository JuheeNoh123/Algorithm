import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
cheeze = []



for i in range(n):
    cheeze.append(list(map(int, input().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    visited = [[ False for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    visited[0][0]=True
    while queue:
        a, b= queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if cheeze[nx][ny]>=1:
                    cheeze[nx][ny]+=1
                else:
                    visited[nx][ny]=True
                    queue.append((nx,ny))

def melt():
    melted=0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j]>=3:
                cheeze[i][j]=0
                melted+=1
            elif cheeze[i][j]==2:
                cheeze[i][j]=1
    return melted
time=0
while True:      
    bfs()
    melted = melt()
    if melted:
        time += 1
    else:
        print(time)
        break