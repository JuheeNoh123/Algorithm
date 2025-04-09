import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
d =[[0,0] for _ in range(100001)]

def bfs(s):
    d[s][1] = 1
    n=s
    
    queue = deque([s])
    
    while queue:
        x = queue.popleft()
        dx=[x,-1,1]
        #print(queue)
        #print(n)
        for i in dx:
            nx = x+i
            #print(nx)
            if 0<=nx and nx<=100000:
                if not d[nx][1]:
                    d[nx][0]=d[x][0]+1
                    d[nx][1] = 1
                    queue.append(nx)
                else:
                    if d[x][0]+1 == d[nx][0]:
                        d[nx][1] += 1
                        queue.append(nx)
                
bfs(a)
print(d[b][0])
print(d[b][1])