import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(m))
def bfs(graph):
   dy=[1,0]
   dx=[0,1]
   queue = deque([(0,0)])
   while queue:
      y,x = queue.popleft()
      #print(x,y)
      
      if y==m-1 and x==n-1:
         return 1
      for i in range(2):
         nx = dx[i]+x
         ny = dy[i]+y
         #print("nx,ny",nx, ny)
         if 0<=nx<len(graph[0]) and 0<=ny<len(graph):
            if graph[ny][nx]!=2 and graph[ny][nx]==1:
               graph[ny][nx] = 2
               queue.append((ny,nx))
               #print(queue)
               
         
   return -1

if bfs(graph)==1:
   print("Yes")
else:
   print("No")

      