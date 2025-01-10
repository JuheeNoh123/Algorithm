import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    L = list(map(int, input().split()))
    for j in range(n):
        if L[j]==1:
            graph[i].append(j)
    
#print(graph)

def bfs(start):
    queue = deque([start])
    visited = [0] * (n)
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i]=1
                queue.append(i)
    return visited

for i in range(n):
    print(* bfs(i))