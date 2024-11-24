import sys
from collections import deque

input = sys.stdin.readline

a,b,n,m = map(int, input().split())
visited = [False for _ in range(100001)]
graph = [0 for _ in range(100001)]
def bfs(x):
    pos = [1,-1,a,-a,b,-b,a,b]
    visited[x] = True
    queue = deque([x])    
    
    while queue:
        v = queue.popleft()
        for i in range(8):
            if i<6:
                y = v + pos[i]
                
            else:
                y = v * pos[i]
            
             
            if 0<=y<=100000 and visited[y] == False:
                visited[y] = True
                queue.append(y)
                graph[y] = graph[v] + 1 
            
    
bfs(n)
print(graph[m])
    