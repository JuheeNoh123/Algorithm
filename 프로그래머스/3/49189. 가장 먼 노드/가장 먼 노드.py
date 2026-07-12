from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1]*(n+1)
    distance[1] = 0
    q = deque([1])
    
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node]==-1:
                distance[next_node] = distance[now]+1
                q.append(next_node)
    m = max(distance[1:])
    return distance[1:].count(m)