from collections import deque

def solution(n, infection, edges, k):
    type_edges = [[], [], [], []]
    for x, y, t in edges:
        type_edges[t].append((x, y))

    # 타입별로 각 노드가 속한 컴포넌트를 '집합'으로 저장
    comp_set = [None, None, None, None]  # comp_set[t][node] = set of nodes

    for t in (1, 2, 3):
        graph = [[] for _ in range(n + 1)]
        for x, y in type_edges[t]:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * (n + 1)
        node_comp = [None] * (n + 1)

        for start in range(1, n + 1):
            if visited[start]:
                continue
            comp_nodes = []
            visited[start] = True
            q = deque([start])
            while q:
                cur = q.popleft()
                comp_nodes.append(cur)
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            comp_nodes_set = set(comp_nodes) #감염 집합체가 모임
            for v in comp_nodes:
                node_comp[v] = comp_nodes_set

        comp_set[t] = node_comp #감염된 노드들을 한번에 조회하기 위해 묶어둠.

    full = set(range(1, n + 1))

    def expand(infected, t):
        node_comp = comp_set[t]
        new_infected = set(infected)
        for v in infected:
            new_infected |= node_comp[v]
        return new_infected

    start = {infection}
    best = len(start)
    memo = set()

    def dfs(infected, depth):
        nonlocal best
        if len(infected) > best:
            best = len(infected)
        if depth == k or infected == full:
            return
        key = (frozenset(infected), depth)
        if key in memo:
            return
        memo.add(key)
        for t in (1, 2, 3):
            dfs(expand(infected, t), depth + 1)

    dfs(start, 0)
    return best