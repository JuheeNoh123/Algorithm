import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline

a,b = map(int, input().split())
x = [list(map(int,input().split())) for _ in range(a)]

#x2=list(x)
#print(x)
L=[]
v=[]
for i in range(a):
    for j in range(b):
        if x[i][j]==0:
            L.append((i,j))
        elif x[i][j]==2:
            v.append((i,j))

def bfs(startx, starty):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    queue = deque([(startx,starty)])
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if 0<=nx<a and 0<=ny<b and x2[nx][ny]==0:
                x2[nx][ny]=2
                queue.append((nx,ny))
    
#print(v)
cnt=0  
for i in combinations(L,3):
    
    x2 = [row[:] for row in x]
    for j in i:
        x2[j[0]][j[1]]=1
    for j in v:
        bfs(j[0],j[1])
    #print(x2)
    total=0
    for i in range(a):
        for j in range(b):
            if x2[i][j]==0:
                total += 1
    cnt = max(cnt,total)
    
    
print(cnt)