import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
L = [[] for _ in range(N+1)] 
# print(L)
nL = [0 for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

visited = [0] * (N+1)
def dfs(start):
    visited[start]=True
    for i in L[start]:
        if visited[i]==False:
            dfs(i)
        else:
            nL[start]=i
dfs(1)
for i in range(2,N+1):
    print(nL[i])
    
