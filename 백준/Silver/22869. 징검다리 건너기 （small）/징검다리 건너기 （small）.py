import sys
from collections import deque
input = sys.stdin.readline

n,k = map (int, input().split())
L = list(map(int, input().split()))
visited = [0]*n
def bfs():
    queue = deque([0])
    
    visited[0]=1
    while queue:
        nq = queue.popleft()    #인덱스
        for i in range(1,k+1):
            if nq+i<n and visited[nq+i]==0 :
                if i*(1+abs(L[nq]-L[nq+i]))<=k:
                    visited[nq+i]=1
                    queue.append(nq+i)
        #print(visited)
        
bfs()

if visited[-1]:
    print("YES")
else:
    print("NO")