import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n,m = map(int, input().split())
L = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int, input().split())
    L[u].append(v)
    L[v].append(u)

visit = [False]*(n+1)
stack = []
def dfs(g, v, s):
    stack.append(s)
    visit[s] = True
    for i in g[s]:
        if not v[i]:
            dfs(g,v,i)
    
cnt = 0
for i in range(1,n+1):
    if i in stack: 
        continue
    else:
        cnt +=1
        dfs(L,visit,i)
print(cnt)