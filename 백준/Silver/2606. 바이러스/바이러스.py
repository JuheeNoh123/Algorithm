import sys
input = sys.stdin.readline

com = int(input())
lines = int(input())

net = [[] for _ in range(com+1)]
visited = [0]*(com+1)

for _ in range(lines):
    idx, num = map(int, input().split())
    
    net[idx].append(num)
    net[num].append(idx)
    
    
def dfs(com_n):
    visited[com_n] = 1
    for i in net[com_n]:
        if visited[i]==0:
            dfs(i)
        

dfs(1)
print(sum(visited)-1)





    