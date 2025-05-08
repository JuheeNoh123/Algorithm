import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited[0][1] = 1

# 1: 가로 
# 2: 세로 
# 3: 대각선

cnt = 0
def dfs(s):
    if s[0]==n-1 and s[1]==n-1:
        global cnt
        cnt+=1
        return
    
    if visited[s[0]][s[1]]==1:
        if s[0]<n and s[1]<n-1 and L[s[0]][s[1]+1]==0:
            visited[s[0]][s[1]+1]=1
            dfs((s[0],s[1]+1))
        if s[0]<n-1 and s[1]<n-1:
            if L[s[0]][s[1]+1]+L[s[0]+1][s[1]]+L[s[0]+1][s[1]+1]==0:
                visited[s[0]+1][s[1]+1]=3
                dfs((s[0]+1,s[1]+1))
    elif visited[s[0]][s[1]]==2:
        if s[0]<n-1 and s[1]<n and L[s[0]+1][s[1]]==0:
            visited[s[0]+1][s[1]] = 2
            dfs((s[0]+1,s[1]))
        if s[0]<n-1 and s[1]<n-1 :
            if L[s[0]][s[1]+1]+L[s[0]+1][s[1]]+L[s[0]+1][s[1]+1]==0:
                visited[s[0]+1][s[1]+1] = 3
                dfs((s[0]+1,s[1]+1))
    elif visited[s[0]][s[1]]==3 :
        if s[0]<n and s[1]<n-1 and L[s[0]][s[1]+1]==0:
            visited[s[0]][s[1]+1] = 1
            dfs((s[0],s[1]+1))
        if s[0]<n-1 and s[1]<n and L[s[0]+1][s[1]]==0:
            visited[s[0]+1][s[1]] = 2
            dfs((s[0]+1,s[1]))
        if s[0]<n-1 and s[1]<n-1 :
            if L[s[0]][s[1]+1]+L[s[0]+1][s[1]]+L[s[0]+1][s[1]+1]==0:
                visited[s[0]+1][s[1]+1] = 3
                dfs((s[0]+1,s[1]+1))

dfs((0,1))

print(cnt)