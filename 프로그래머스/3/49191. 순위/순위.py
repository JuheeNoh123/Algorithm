from collections import defaultdict

def dfs(start, graph):
    visited = set()
    stack = [start]
    while stack:
        now = stack.pop()
        for next_node in graph[now]:
            if next_node not in visited:
                stack.append(next_node)
                visited.add(next_node)
    return visited

def solution(n, results):
    answer = 0
    win = defaultdict(set) #win[a] a가 이긴 선수들
    lose = defaultdict(set) #lose[a] a가 진 선수들
    for w,l in results:
        win[w].add(l)
        lose[l].add(w)
    
    for player in range(1,n+1):
        b = dfs(player, win) #player가 이긴 모든 선수, 간접 포함
        bb = dfs(player, lose) #player가 진 모든 선수, 간접 포함
        if len(b)+len(bb)==n-1:
            answer +=1
        #print(b,bb)
    
    return answer