import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int, input().split())
L=[]
for i in range(n):
   L.append(list(map(int, input().split())))

dx,dy=[0,0,1,-1],[1,-1,0,0]   

def bfs(starty, startx):
   sum,lenth=0,0

   queue = deque([(starty,startx)])
   visited = [[0 for _ in range(m)] for _ in range(n)]
   
   visited[starty][startx]=1
   
   while queue:
      y,x = queue.popleft()
      
      for i in range(4):
         nx, ny = x+dx[i], y+dy[i]
         
         if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and L[ny][nx]:
            visited[ny][nx]=visited[y][x]+1
            rlwhs=lenth
            lenth = max(lenth, visited[ny][nx])
            if rlwhs!=lenth:
               sum=L[ny][nx]+L[starty][startx]
            queue.append((ny,nx))
            
            #print(visited)
   if lenth==0:
      return (L[starty][startx]*2,0)
   #print(visited)
   return (sum, lenth)



maxLenth=0
maxSum=0
for i in range(n):
   for j in range(m):
      if L[i][j]:
         sum, lenth = bfs(i,j)

         if lenth>maxLenth:
            maxLenth = lenth
            maxSum = sum
         elif lenth==maxLenth:
            maxSum = max(sum,maxSum)
            
         
print(maxSum)
         
