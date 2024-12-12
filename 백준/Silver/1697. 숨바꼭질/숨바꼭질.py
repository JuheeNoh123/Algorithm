import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
visited = [False for _ in range(100001)]
graph = [0 for _ in range(100001)]
def bfs(x):
    
    visited[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for x in (v-1,v+1,v*2):
            if 0<=x<=100000 and not visited[x]:
                visited[x] = True
                queue.append(x)
                graph[x] = graph[v]+1
                
bfs(n)
print(graph[k])