import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph=[0 for _ in range(101)]
cnt=[0]*101
visited = [False]*101
snake=[]
def bfs(start):
    queue = deque([start])
    visited[start]=True
    
    while queue:
        num = queue.popleft()
        for i in range(1,7):
            if num+i<=100:
                if not visited[num+i]:
                    visited[num+i]=True
                    if not (num+i in snake):
                        queue.append(num+i)
                    cnt[num+i]=cnt[num]+1
                    if graph[num+i] and not visited[graph[num+i]]:
                        visited[graph[num+i]]=True
                        cnt[graph[num+i]]=cnt[num+i]
                        
                        queue.append(graph[num+i])
                        
                        
        # print(queue)     
        # print(cnt)
                    
            
            
        
for i in range(N+M):
    a, b = map(int, input().split())
    graph[a]=b
    
    snake.append(a)
    

bfs(1)

print(cnt[-1])